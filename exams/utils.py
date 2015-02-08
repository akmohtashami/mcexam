import subprocess
import os


def compile_tex(tex_content, output_directory, output_file_name, env=os.environ):
    compiler = subprocess.Popen(["xelatex", "-jobname=" + output_file_name], env=env, cwd=output_directory,
                                stdin=subprocess.PIPE,
                                stderr=subprocess.PIPE,
                                stdout=subprocess.PIPE)
    return compiler.communicate(input=tex_content)


