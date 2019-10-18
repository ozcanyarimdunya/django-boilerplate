# Project

A boilerplate django project.


## Local setup

1. Install the virtualenv package.
   ```
   pip install virtualenv
   ```

2. Create the virtual environment.
   ```
   virtualenv venv
   ```    

3. Activate the virtual environment.
   ```
   source venv/bin/activate
   ```

4. Install all dependencies and start application.
   ```
   make
   ```

## Docker installation

1. Make sure you have installed **docker**.
   ```
   make docd
   ```

## Documentations

1. Add document files under **docs/** folder and build them as html.
   ```
   pip install sphinx
   ```
   ```
   make documentation
   ```
