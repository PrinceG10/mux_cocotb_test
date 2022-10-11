TOPLEVEL=mux
MODULE=test

VERILOG_SOURCES +=mux.v

SIM ?= icarus
TOPLEVEL_LANG ?= verilog
include $(shell cocotb-config --makefiles)/Makefile.sim
