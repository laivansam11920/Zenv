import { arrayBufferToBase64 } from '../utils/arrayBufferToBase64.js'


async function encryptEnvFile(envContent) {
    const encoder = new TextEncoder();
    const data = encoder.encode(envContent);

    const key = await window.crypto.subtle.generateKey(
        { name: "AES-GCM", length: 256 },
        true,
        ["encrypt", "decrypt"]
    );

    const iv = window.crypto.getRandomValues(new Uint8Array(12));

    const encryptedBuffer = await window.crypto.subtle.encrypt(
        { name: "AES-GCM", iv: iv },
        key,
        data
    );

    const combinedBuffer = new Uint8Array(iv.length + encryptedBuffer.byteLength);
    combinedBuffer.set(iv, 0);
    combinedBuffer.set(new Uint8Array(encryptedBuffer), iv.length);

    const exportedKey = await window.crypto.subtle.exportKey("raw", key);
    const keyBase64 = arrayBufferToBase64(exportedKey);

    const encryptedDataBase64 = arrayBufferToBase64(combinedBuffer.buffer);

    return {
        encryptedData: encryptedDataBase64,
        secretKey: keyBase64
    };
}

export default encryptEnvFile