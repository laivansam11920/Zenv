
import encryptEnvFile from './encrypt/main.js';
import decryptEnvFile from './decrypt/main.js';

const fileInput = document.getElementById('fileInput');
const rawEnvEl = document.getElementById('rawEnv');
const encryptedDataEl = document.getElementById('encryptedData');
const decryptedTextEl = document.getElementById('decryptedText');

fileInput.addEventListener('change', function(event) {
    const file = event.target.files[0];

    if (file) {
        const reader = new FileReader();

        reader.onload = async function(e) {

            const rawEnv = e.target.result.trim();
            rawEnvEl.textContent = rawEnv;

            const result = await encryptEnvFile(rawEnv, 'Hello');

            encryptedDataEl.textContent = result.encryptedData;

            const decryptedText = await decryptEnvFile(result.encryptedData, 'Hello');
            decryptedTextEl.textContent = decryptedText;

            console.log("=== 1. FILE ORIGIN (.env) ===");
            console.log(rawEnv);
            console.log("\n=== 2. KẾT QUẢ MÃ HÓA ===");
            console.log("File mã hóa:", result.encryptedData);
            console.log("\n=== 3. KẾT QUẢ GIẢI MÃ ===");
            console.log(decryptedText);
        };

        reader.readAsText(file);
    }
});