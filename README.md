### Bootstrapping

##### Requirements
- Create virtual environment and install requirements
 
- Local memcached: 
    - `sudo apt update && upgrade`
    - `sudo apt install memcached`
    - default configuration it's ok
    - check if it's running: `sudo systemctl status memcached`
    - *[optional]* list all defined keys: `sudo apt install libmemcached-tools` and `memcdump --servers=localhost`
     

##### Environment variables
- Crete file called .env in root directory and copy the content of .env.example file into it
- Ask for api keys

### Running

Run command `flask run` in terminal or config PyCharm runner for Flask apps
