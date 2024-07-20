from articlib.testEngine import test
import shutil

def runTest():
    print("Starting information table test")
    runScenario1()
    runScenario2()
    print("Information table test finished")
    
def runScenario1():
    test.newScenario("Create an information")
    test11_13()
    test14()
    test15()
    test.endScenario("Create an information")

def runScenario2():
    test.newScenario("Get information information")
    test21_29()
    test.endScenario("Get information information")
    
def test11_13():
    pass

def test14():
    pass

def test15():
    pass

def test21_29():
    pass

if __name__ == "__main__":
    shutil.copy("emptyDatabase.db", "test.db")
    runTest()
    test.printResults()
    