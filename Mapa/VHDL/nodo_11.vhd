-- nodo_11.vhdl : Achivo VHDL generado automaticamente
library IEEE;
use IEEE.std_logic_1164.all;
use IEEE.numeric_std.all;
--Declare the package
use work.my_package.all;
	entity nodo_11 is
		generic(
			N : natural := 40;
			N_SEM : natural := 12;
			N_MDC : natural := 4;
			N_CVS : natural := 12
		);
		port(
			Clock :  in std_logic;
			Reset :  in std_logic;
			Estado_i :  in std_logic;
			Estado_ante :  in std_logic;
			Estado_post :  in std_logic;
			Estado_o :  out std_logic
		);
	end entity nodo_11;
architecture Behavioral of nodo_11 is
begin
	Estado_o <= Estado_i;
end Behavioral;