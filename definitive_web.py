# import standard resources
import os
import subprocess
from flask import Flask, render_template, request

# import our utility functions and constants
from lib.utils import generate_random_string, is_word, is_word_class, is_definition, is_see_also, is_avatar, validate_inputs, hold_on
from lib.config import (WHITELIST_TMP, ID_STRING_LENGTH, PYTHON_CMD, RENDER_CMD, RENDER_OPT_WORD_CLASS,  ERROR_WORD, ERROR_WORD_CLASS, 
                        ERROR_DEFINITION, ERROR_SEE_ALSO, ERROR_AVATAR, WORD_MAX_LENGTH, DEFINITION_MAX_LENGTH, SEE_ALSO_MAX_LENGTH, IMG_TEXT_COLOR,
                        IMG_BORDER_COLOR, IMG_TOP_MARGIN, BASE_DELAY, MAX_DELAY_DELTA)

app = Flask(__name__)

# receive a POST request with the fields necessary for the definition
# and return the new html for the div
@app.route('/render', methods=['POST'])
def render():
    form_word = request.form['word']
    form_word_class = request.form['word_class']
    form_definition = request.form['definition']
    form_see_also = request.form['see_also']
    form_avatar = request.form['avatar'].lower()

    basename = 'img'
    subdir = 'user-img'
    random_id = generate_random_string(ID_STRING_LENGTH, WHITELIST_TMP)

    # validate input and return a standard error if the input is not fine
    status = validate_inputs(form_word, form_word_class, form_definition, form_see_also, form_avatar)

    # TODO
    # 0. cronjob to delete the older ones (>10m) + PATH security

    # path where the output image will be saved
    # it needs to be derived automatically from the filesystem location
    base_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static')
    render_opt_output = f"-o{base_path}/{subdir}/{basename}-{random_id}.png"

    # we either render an error image or the image request by the user
    if status is False:
        print('error situation')
        word = ERROR_WORD
        word_class = ERROR_WORD_CLASS
        definition = ERROR_DEFINITION
        see_also = ERROR_SEE_ALSO
        avatar = ERROR_AVATAR
    else:
        print('normal situation')
        word_class = form_word_class
        word = form_word
        definition = form_definition
        see_also = form_see_also
        avatar = form_avatar

    render_opt_word = f"-w{word}"
    render_opt_word_class = f"-c{word_class}"
    render_opt_definition = f"-d{definition}"
    render_opt_see_also = f"-s{see_also}"
    render_opt_others = f"--font-color={IMG_TEXT_COLOR}"

    arg_list = [PYTHON_CMD, RENDER_CMD, render_opt_word, render_opt_word_class, render_opt_definition, render_opt_see_also, render_opt_output, render_opt_others ]

    if avatar != 'none':
        render_opt_avatar = f"-a{avatar}"
        arg_list.append(render_opt_avatar)

    # sleep for a "small" amount of time to prevent overwhelming the system
    # (it can still be overused but in a different way)
    hold_on(BASE_DELAY, MAX_DELAY_DELTA)

    # the subprocess needs to have as working directory the place where the executable lives
    # because it uses a relative path inside, for the avatar images
    subprocess.run(arg_list, cwd=os.path.dirname(RENDER_CMD))

    return render_template('img-div.html.j2', subdir=subdir, basename=basename, id=random_id, img_border_color=IMG_BORDER_COLOR, img_top_margin=IMG_TOP_MARGIN)


@app.route('/')
def main_page():

    return render_template('main.html.j2', title="Definitive", subtitle="A place for less than serious definitions",
                           word_max_length=WORD_MAX_LENGTH, definition_max_length=DEFINITION_MAX_LENGTH,
                           see_also_max_length=SEE_ALSO_MAX_LENGTH, border_color=IMG_BORDER_COLOR, img_top_margin=IMG_TOP_MARGIN)


if __name__ == '__main__':
   app.run(debug=False, host='0.0.0.0')