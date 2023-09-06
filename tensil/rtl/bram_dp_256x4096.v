// Dual-Port Block RAM with Two Write Ports
// File: rams_tdp_rf_rf.v
module bram_dp_256x4096 (clka,clkb,ena,enb,wea,web,addra,addrb,dia,dib,doa,dob);
input clka,clkb,ena,enb,wea,web;
input [11:0] addra,addrb;
input [255:0] dia,dib;
output [255:0] doa,dob;
reg [255:0] ram [4095:0];
reg [255:0] doa,dob;

always @(posedge clka)
begin
  if (ena)
    begin
      if (wea)
        ram[addra] <= dia;
      doa <= ram[addra];
    end
end

always @(posedge clkb)
begin
  if (enb)
    begin
      if (web)
        ram[addrb] <= dib;
      dob <= ram[addrb];
    end
end
endmodule