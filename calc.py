from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import operator

from Design import Ui_App_Calc

READY = 0
INPUT = 1

class Calc_function(QMainWindow, Ui_App_Calc):
    def __init__(self, *args, **kwargs):
        super(Calc_function, self).__init__(*args, **kwargs)
        self.setWindowIcon(QIcon('calc.jpg'))
        self.setupUi(self)
        self.state = True
        
        for n in range(0, 10):
            getattr(self, 'b_%s' % n).pressed.connect(lambda v=n: self.input_number(v))
        self.b_01.pressed.connect(lambda v=0.1: self.input_number(v))
        
        self.b_plus.pressed.connect(lambda: self.operation(operator.add))
        self.b_subtr.pressed.connect(lambda: self.operation(operator.sub))
        self.b_multiply.pressed.connect(lambda: self.operation(operator.mul))
        self.b_divide.pressed.connect(lambda: self.operation(operator.truediv))
        self.b_percent.pressed.connect(self.operation_pc)
        self.b_equals.pressed.connect(self.equals)
        
        self.b_c.pressed.connect(self.reset)
        self.b_m.pressed.connect(self.memory_store)
        self.b_mr.pressed.connect(self.memory_recall)
        self.memory = 0
        self.reset()
        self.show()
        
    def display(self):
        self.numbers.display(self.stack[-1])

    def reset(self):
        self.state = READY
        self.stack = [0]
        self.last_operation = None
        self.current_op = None
        self.display()

    def memory_store(self):
        self.memory = self.numbers.value()

    def memory_recall(self):
        self.state = INPUT
        self.stack[-1] = self.memory
        self.display()

    def input_number(self, v):
        if self.state == READY:
            self.state = INPUT
            self.stack[-1] = v
        else:
            self.stack[-1] = self.stack[-1] * 10 + v

        self.display()

    def operation(self, op):
        if self.current_op:
            self.equals()

        self.stack.append(0)
        self.state = INPUT
        self.current_op = op

    def operation_pc(self):
        self.state = INPUT
        self.stack[-1] *= 0.01
        self.display()

    def equals(self):
        if self.state == READY and self.last_operation:
            s, self.current_op = self.last_operation
            self.stack.append(s)

        if self.current_op:
            self.last_operation = self.stack[-1], self.current_op
            try:
                self.stack = [self.current_op(*self.stack)]
            except Exception:
                self.numbersr.display('Err')
                self.stack = [0]
            else:
                self.current_op = None
                self.state = READY
                self.display()      
                
if __name__ == '__main__':
    app = QApplication([])
    app.setApplicationName("Считалка")
    window = Calc_function()
    app.exec_()
    
