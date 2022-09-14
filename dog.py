with open("cat.py","w") as fii:
    fii.write("class bark:\n")
    fii.write("    def cat(dog='bark'):\n")
    fii.write("        print(dog)\n")
    fii.write("        input()\n")
    fii.write("if(__name__=='__main__'):\n")
    fii.write("    bark.cat()\n")
import cat
dog=cat.bark
dog=dog.cat("meow")
