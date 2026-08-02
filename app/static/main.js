import encryptEnvFile from './encrypt/main.js'
import decryptEnvFile from './decrypt/main.js'

(async () => {
    const rawEnv = `
PORT=5000
DATABASE_URL=postgres://user:pass@localhost:5432/mydb
SECRET_KEY=super_secret_key_12345
    `.trim();

    console.log("=== 1. FILE ORIGIN (.env) ===");
    console.log(rawEnv);

    const result = await encryptEnvFile(rawEnv);

    console.log("\n=== 2. KẾT QUẢ MÃ HÓA ===");
    console.log("File mã hóa (Up lên Server):", result.encryptedData);
    console.log("Chìa khóa Secret (Trả cho User):", result.secretKey);

    const decryptedText = await decryptEnvFile(result.encryptedData, result.secretKey);

    console.log("\n=== 3. KẾT QUẢ GIẢI MÃ ===");
    console.log(decryptedText);
})();