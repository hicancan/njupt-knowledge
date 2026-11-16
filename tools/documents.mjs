// Read the authored Markdown with the same document kernel used by every reader.
import { readFile } from 'node:fs/promises';
import { initialize, read } from 'docstream';

await initialize(new Uint8Array(await readFile(new URL(import.meta.resolve('docstream/docstream_wasm_bg.wasm')))));
const input = [];
for await (const chunk of process.stdin) input.push(chunk);
const documents = JSON.parse(Buffer.concat(input).toString('utf8'));
const plain = inlines => inlines.map(inline => inline.text ?? inline.tex ?? inline.alt ?? (inline.children ? plain(inline.children) : inline.type === 'break' ? '\n' : '')).join('');
function links(value, out = []) {
    if (!value || typeof value !== 'object') return out;
    if (Array.isArray(value)) { value.forEach(item => links(item, out)); return out; }
    if (value.type === 'link') out.push(value.href);
    if (value.type === 'image') out.push(value.src);
    for (const child of Object.values(value)) links(child, out);
    return out;
}
function events(blocks, out = []) {
    for (const block of blocks) {
        if (block.type === 'heading') out.push({ type: 'heading', level: block.level, title: plain(block.inlines), anchor: block.anchor, links: links(block) });
        else if (block.type === 'paragraph') out.push({ type: 'paragraph', text: plain(block.inlines), links: links(block) });
        else {
            out.push({ type: 'links', links: links(block) });
            if (block.blocks) events(block.blocks, out);
            if (block.items) block.items.forEach(item => events(item.blocks, out));
        }
    }
    return out;
}
function images(value, out = []) {
    if (!value || typeof value !== 'object') return out;
    if (Array.isArray(value)) { value.forEach(item => images(item, out)); return out; }
    if (value.type === 'image') out.push(value.src);
    for (const child of Object.values(value)) images(child, out);
    return out;
}
process.stdout.write(JSON.stringify(documents.map(document => {
    const blocks = read(document.body);
    return { path: document.path, events: events(blocks), images: images(blocks) };
})));
