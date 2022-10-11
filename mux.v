// Simple mux DUT
module mux(input I0, I1,S,
                 output O);
  assign O = S? I1 : I0;

endmodule
