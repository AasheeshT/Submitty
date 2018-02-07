import subprocess
import sys
import os
from shutil import copyfile

cwd = os.getcwd()

clangDir = os.path.expanduser("/usr/local/submitty/clang-llvm/")


#astMatcherDir = os.path.expanduser(clangDir + "llvm/tools/clang/tools/extra/ASTMatcher/")

#if not os.path.exists(astMatcherDir):
        #os.mkdir(astMatcherDir)


#copyfile("/usr/local/submitty/GIT_CHECKOUT_AnalysisTools/commonAST/CMakeLists.txt", astMatcherDir + "CMakeLists.txt")
#copyfile("/usr/local/submitty/GIT_CHECKOUT_AnalysisTools/commonAST/ASTMatcher.cpp", astMatcherDir + "ASTMatcher.cpp")

os.chdir(clangDir + "build/")

subprocess.call(["ninja"])

os.chdir(cwd)
