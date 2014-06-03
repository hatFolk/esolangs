import pyBf

def ooktoBf(text):
    options = {("Ook.","Ook?"):">",
            ("Ook?","Ook."):"<",
            ("Ook.","Ook."):"+",
            ("Ook!","Ook!"):"-",
            ("Ook!","Ook."):".",
            ("Ook.","Ook!"):",",
            ("Ook!","Ook?"):"[",
            ("Ook?","Ook!"):"]"}
    text = text.replace("\n", " ")[:-1].split(" ")
    text = [i for i in text if i != ""] # This seems wasteful.
    x  = [options.get((text[i], text[i+1]), "") for i in range(0, len(text)-1, 2)]
    return "".join(x)

def main(files):
    [i for i in map(lambda x: pyBf.parse(ooktoBf(pyBf.openFile(x))), files)]

if __name__=="__main__": main(pyBf.sys.argv[1:])
