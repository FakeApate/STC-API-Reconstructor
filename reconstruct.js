//100% ChatGPT 4.0 generated.
const fs = require('fs');
const path = require('path');
const { SourceMapConsumer } = require('source-map');

const folderPath = 'out/';

// Read all files from the folder
fs.readdir(folderPath, (err, files) => {
    if (err) {
        console.error("Could not list the directory.", err);
        process.exit(1);
    }

    files.forEach(file => {
        // Process only .map files
        if (path.extname(file) === '.map') {
            const mapFilePath = path.join(folderPath, file);
            fs.readFile(mapFilePath, 'utf8', (err, data) => {
                if (err) {
                    console.error(`Error reading file ${mapFilePath}`, err);
                    return;
                }

                try {
                    const sourceMap = JSON.parse(data);
                    SourceMapConsumer.with(sourceMap, null, consumer => {
                        consumer.sources.forEach(source => {
                            if(source.startsWith("..")){
                                console.log(`Skipping ${source}`);
                                return;
                            }
                            // For each source file in the source map, extract and save the original content
                            const content = consumer.sourceContentFor(source);
                            const outputPath = path.join(folderPath, 'originals', source);
                            const outputDir = path.dirname(outputPath);

                            // Ensure the directory exists
                            fs.mkdirSync(outputDir, { recursive: true });

                            // Write the original source content to a new file
                            fs.writeFile(outputPath, content, err => {
                                if (err) {
                                    console.error(`Error writing file ${outputPath}`, err);
                                } else {
                                    console.log(`Reconstructed ${outputPath}`);
                                }
                            });
                        });
                    });
                } catch (error) {
                    console.error(`Error processing source map ${mapFilePath}`, error);
                }
            });
        }
    });
});
