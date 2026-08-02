import { arrayBufferToBase64 } from '../utils/arrayBufferToBase64.js';

async function encryptEnvFile(envContent, password) {
    const encoder = new TextEncoder();
    const data = encoder.encode(envContent);

    const salt = window.crypto.getRandomValues(new Uint8Array(16));
    const iv = window.crypto.getRandomValues(new Uint8Array(12));

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
        ["encrypt"]
    );

    const encryptedBuffer = await window.crypto.subtle.encrypt(
        { name: "AES-GCM", iv: iv },
        key,
        data
    );

    const combinedBuffer = new Uint8Array(salt.length + iv.length + encryptedBuffer.byteLength);
    combinedBuffer.set(salt, 0);
    combinedBuffer.set(iv, salt.length);
    combinedBuffer.set(new Uint8Array(encryptedBuffer), salt.length + iv.length);

    const encryptedDataBase64 = arrayBufferToBase64(combinedBuffer.buffer);

    return {
        encryptedData: encryptedDataBase64
    };
}

export default encryptEnvFile;