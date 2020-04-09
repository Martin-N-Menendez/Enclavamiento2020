-- nodo_13.vhdl : Achivo VHDL generado automaticamente
library IEEE;
use IEEE.std_logic_1164.all;
use IEEE.numeric_std.all;
--Declare the package
use work.my_package.all;
	entity nodo_13 is
		generic(
			N : natural := 50;
			N_SEM : natural := 16;
			N_MDC : natural := 4;
			N_CVS : natural := 14
		);
		port(
			Clock :  in std_logic;
			Reset :  in std_logic;
			Estado_i :  in std_logic;
			Estado_ante :  in std_logic;
			Estado_post :  in std_logic;
			Estado_o :  out std_logic
		);
	end entity nodo_13;
architecture Behavioral of nodo_13 is
begin
	Estado_o <= Estado_i;
end Behavioral;