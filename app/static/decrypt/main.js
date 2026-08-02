import { base64ToArrayBuffer } from "../utils/base64ToArrayBuffer.js";

async function decryptEnvFile(encryptedDataBase64, keyBase64) {
    const decoder = new TextDecoder();

    const keyBuffer = base64ToArrayBuffer(keyBase64);
    const key = await window.crypto.subtle.importKey(
        "raw",
        keyBuffer,
        { name: "AES-GCM" },
        false,
        ["decrypt"]
    );

    const combinedBuffer = new Uint8Array(base64ToArrayBuffer(encryptedDataBase64));
    const iv = combinedBuffer.slice(0, 12);
    const ciphertext = combinedBuffer.slice(12);

    const decryptedBuffer = await window.crypto.subtle.decrypt(
        { name: "AES-GCM", iv: iv },
        key,
        ciphertext
    );

    return decoder.decode(decryptedBuffer);
}

export default decryptEnvFile