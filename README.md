# Firestore Database Importer

This is a simple and tested nodejs app for importing JSON data into a Firestore Collection.

## Credits 
- Utilizing this wonderful package https://github.com/dalenguyen/firestore-backup-restore this code is possible. Dalenguyen deserves credits for his work. The Github documentation is great and they give a few other scenarios for data movement. 

## Recommended Setup

- Clone the repo and run npm install to install dependencies
- Assuming you already have a Firebase Account and Project, you will need your serviceAccount.json file.
- You may not need the basic Firebase credentials to put in the config.js for the database url because the serviceAccount should contain the required data paths. 
- You will need your data that needs imported saved in .json file. Read the comments in import.js for replacing your collection.json <--what ever name you have for your file. 

## Important
- NOTE: I have placed a .gitignore here already, but always ensure you protect your serviceAccount.json keys before uploading code to Github or other Repositories.

## Running the app
I have a start script included in the package.json. Or you can run "node import.js" in your terminal. The console logs will show initialization and progress. Check your Firestore Database for collection importing. 

## Fake Data Generator for testing
- I have included a fake_data_generator.py file for generating some test data, you might need to install faker for python and also have the current version of Python installed. You can run that file in the terminal. It will output the fake_data_json (Randomly Generated JSON data) into the project folder. This file could be modified to the data you need to generate. 

## Special attention
- Make sure you read your Firebase documentation in regards to Firestore Database charges for data read and writes. The limits are very high but you don't want to be surprised. 

## Happy Coding
I hope this helps in a pinch or use the code as an example and create your own.