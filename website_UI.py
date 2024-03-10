import streamlit as st
import os
import subprocess

def save_uploaded_file(uploaded_file):
    with open(os.path.join("tempDir", uploaded_file.name), "wb") as f:
        f.write(uploaded_file.getbuffer())
    return os.path.join("tempDir", uploaded_file.name)

# Setup Streamlit UI
st.title('Jupyter Notebook Translator')

# Create a directory for saving uploaded files if it doesn't already exist
if not os.path.exists('tempDir'):
    os.makedirs('tempDir')

uploaded_file = st.file_uploader("Choose a Jupyter notebook file", type=['ipynb'])
if uploaded_file is not None:
    file_path = save_uploaded_file(uploaded_file)
    st.success('File uploaded successfully.')

languages = {'af': 'afrikaans',
 'sq': 'albanian',
 'am': 'amharic',
 'ar': 'arabic',
 'hy': 'armenian',
 'az': 'azerbaijani',
 'eu': 'basque',
 'be': 'belarusian',
 'bn': 'bengali',
 'bs': 'bosnian',
 'bg': 'bulgarian',
 'ca': 'catalan',
 'ceb': 'cebuano',
 'ny': 'chichewa',
 'zh-cn': 'chinese (simplified)',
 'zh-tw': 'chinese (traditional)',
 'co': 'corsican',
 'hr': 'croatian',
 'cs': 'czech',
 'da': 'danish',
 'nl': 'dutch',
 'en': 'english',
 'eo': 'esperanto',
 'et': 'estonian',
 'tl': 'filipino',
 'fi': 'finnish',
 'fr': 'french',
 'fy': 'frisian',
 'gl': 'galician',
 'ka': 'georgian',
 'de': 'german',
 'el': 'greek',
 'gu': 'gujarati',
 'ht': 'haitian creole',
 'ha': 'hausa',
 'haw': 'hawaiian',
 'iw': 'hebrew',
 'hi': 'hindi',
 'hmn': 'hmong',
 'hu': 'hungarian',
 'is': 'icelandic',
 'ig': 'igbo',
 'id': 'indonesian',
 'ga': 'irish',
 'it': 'italian',
 'ja': 'japanese',
 'jw': 'javanese',
 'kn': 'kannada',
 'kk': 'kazakh',
 'km': 'khmer',
 'ko': 'korean',
 'ku': 'kurdish (kurmanji)',
 'ky': 'kyrgyz',
 'lo': 'lao',
 'la': 'latin',
 'lv': 'latvian',
 'lt': 'lithuanian',
 'lb': 'luxembourgish',
 'mk': 'macedonian',
 'mg': 'malagasy',
 'ms': 'malay',
 'ml': 'malayalam',
 'mt': 'maltese',
 'mi': 'maori',
 'mr': 'marathi',
 'mn': 'mongolian',
 'my': 'myanmar (burmese)',
 'ne': 'nepali',
 'no': 'norwegian',
 'ps': 'pashto',
 'fa': 'persian',
 'pl': 'polish',
 'pt': 'portuguese',
 'pa': 'punjabi',
 'ro': 'romanian',
 'ru': 'russian',
 'sm': 'samoan',
 'gd': 'scots gaelic',
 'sr': 'serbian',
 'st': 'sesotho',
 'sn': 'shona',
 'sd': 'sindhi',
 'si': 'sinhala',
 'sk': 'slovak',
 'sl': 'slovenian',
 'so': 'somali',
 'es': 'spanish',
 'su': 'sundanese',
 'sw': 'swahili',
 'sv': 'swedish',
 'tg': 'tajik',
 'ta': 'tamil',
 'te': 'telugu',
 'th': 'thai',
 'tr': 'turkish',
 'uk': 'ukrainian',
 'ur': 'urdu',
 'uz': 'uzbek',
 'vi': 'vietnamese',
 'cy': 'welsh',
 'xh': 'xhosa',
 'yi': 'yiddish',
 'yo': 'yoruba',
 'zu': 'zulu',
 'fil': 'Filipino',
 'he': 'Hebrew'}
# Select target language
target_language = st.selectbox('Select target language', options=list(languages.keys()), index=list(languages.keys()).index('en'), format_func=lambda x: languages[x])

if st.button('Translate'):
    if uploaded_file is not None and target_language:
        try:
            output_file_path = file_path.replace('.ipynb', f'_{target_language}.ipynb')
            # Command to run the jupyter_translate script

            command = f'python jupyter_translate.py {file_path} --language "{target_language}"'
            process = subprocess.run(command, shell=True, check=True, text=True, capture_output=True)
            st.write('process completed!')
            if process.returncode == 0:
                st.write('Translation completed!')
                with open(output_file_path) as f:
                # Provide a download button for the translated notebook
                    st.download_button(label="Download Translated Notebook", data=f, file_name=os.path.basename(output_file_path), mime='application/octet-stream')
                st.success('Translation completed!')
            else:
                st.error(f'Translation failed: {process.stderr}')
        except Exception as e:
            st.error(f'Error during translation: {e}')
    else:
        st.error('Please upload a file and select a target language.')
