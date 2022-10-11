import cocotb


from cocotb.triggers import Timer

from cocotb.result import TestFailure

@cocotb.test()
def dir_mux (dut): 
    
    dut.log.info("Start of test!")
    yield Timer(10000)
    dut.log.info("Drive 1 & 0 to input I1 and I2 and select line S=0!")
    
    dut.I0= 1
    dut.I1 = 0
    dut.S = 0
    yield Timer(10000)
    
    if dut.O != 1:
        raise TestFailure("mux incorrect: %s != 0" % str(dut.c)) 
    else:
        dut.log.info("PASS!")
    dut.log.info("Drive 1 & 0 input I1 and I2 and select line S=1!")
    dut.I0 = 1
    dut.I1= 0
    dut.S = 1 
    
    # Wait for 10 ns
    yield Timer(10000)
    
    # Use wrong EXPECT - to see some failure in Cocotb for fun!
    if dut.O!= 0:
        raise TestFailure("mux test failed %s != 0" % str(dut.c)) 
    else: # these last two lines are not strictly necessary
        dut.log.info("PASS!")
