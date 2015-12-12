from subprocess import call
from os.path import join as create_path
from os.path import basename as base
from os.path import splitext as split

try:
    from langdetect import detect
except:
    print "**installing langdetect package**"
    try:
        call(["pip","install","langdetect"])
    except:
        print "**installation failed, exiting**"
        exit(1)

class Classifier(object):
    
    def __init__(self, image_name=None, user_id=None):
        self.image_name = image_name
        
        self.path_to_img_translation = create_path(split(base(image_name))[0]+"_translation")
        self.langs = {'es':'spanish','fr':'french','en':'english','du':'dutch'}
        

    def build_directory():
        try:
            call(["mkdir","-p",path_to_translations])
        except:
            print "error building translation directory"
            exit(1)

    def extract_text(self):
        try:
            call(["tesseract", self.image_name, self.path_to_img_translation])
        except OSError:
            print "Please run \'brew install tesseract\'"
            exit(1)

    def classify_text(self):
        self.extract_text()
        ff = open(self.path_to_img_translation+".txt", 'r')
        text = str(ff.read())
        text = text.decode("utf-8")
        translation = detect(text)
        try:
            return self.langs[translation]
        except:
            return translation

    def output_translation():
        pass
    

def main():
    cc = Classifier("spanish.png")
    print cc.classify_text()


if __name__ == "__main__":
    main()
