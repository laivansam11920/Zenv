import { base64ToArrayBuffer } from '../utils/base64ToArrayBuffer.js';

async function decryptEnvFile(encryptedDataBase64, password) {
    const encoder = new TextEncoder();
    const decoder = new TextDecoder();

    const combinedBuffer = new Uint8Array(base64ToArrayBuffer(encryptedDataBase64));

    const salt = combinedBuffer.subarray(0, 16);
    const iv = combinedBuffer.subarray(16, 28);
    const ciphertext = combinedBuffer.subarray(28);

    const passwordKey = await window.crypto.subtle.importKey(
        "raw",
        encoder.encode(password),
        { name: "PBKDF2" },
        false,
        ["deriveKey"]
    );

    const key = await window.crypto.subtle.deriveKey(
        {
            name: "PBKDF2",
            salt: salt,
            iterations: 100000,
            hash: "SHA-256"
        },
        passwordKey,
        { name: "AES-GCM", length: 256 },
        false,
        ["decrypt"]
    );

    const decryptedBuffer = await window.crypto.subtle.decrypt(
        { name: "AES-GCM", iv: iv },
        key,
        ciphertext
    );

    return decoder.decode(decryptedBuffer);
}

export default decryptEnvFile;