# 🧿 AWAVE
## 🌈 audio2waveform
### 📚 Description
Web Application project that allow you upload a .wav file to generate the respectively circular waveform as .png 
### 📋 Requirements & 📥 Installation
#### Requirements
To use awave, you need to have the following requirements installed on your system:
- Git - Git Bash (run as administrator)
- Microsoft Visual C++ 14.0
- Python 3.6 or higher
    - Flask
    - OpenCV
    - NumPy
    - SciPy
    - Werkzeug

To install the required dependencies, you can use pip (the package installer for Python). 
Open your terminal or command prompt and run the following command:
If you don't have Python installed on your system, you can download it from [python](https://www.python.org/downloads/).
Could be also needed [Win C++](https://visualstudio.microsoft.com/it/visual-cpp-build-tools/) only if needed
If you don't have pip installed on your system, you can download it with the following command:
```python
python get-pip.py
```
#### Installation
1. Clone the "awave" repository to your local machine.
```bash
git clone https://github.com/DiMo1999/awave
```
2. Navigate to the project directory in your terminal.
```bash
cd awave 
```
3. Run the following command to start the application:
```python
pip install -r requirements.txt
python app.py
```

### 🚀 Usage
1. Open your web browser and go to `http://localhost:5000`.
2. Adjust the zoom factor if needed.
3. Drop the audio file you want to upload in the droparea.
4. Wait for the waveform to be generated.
5. The generated waveform image will be displayed on the page automatically

### 📝 License
"awave" is licensed under the GNU GENERAL PUBLIC LICENSE License. See the [LICENSE](LICENSE) file for more details.
