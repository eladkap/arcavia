class Loader {
    static async loadJsonFile(jsonFilePath) {
        const response = await fetch(jsonFilePath);
        return response.json();
    }
}