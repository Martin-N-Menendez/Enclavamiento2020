-- nodo_2.vhdl : Achivo VHDL generado automaticamente
library IEEE;
use IEEE.std_logic_1164.all;
use IEEE.numeric_std.all;
--Declare the package
use work.my_package.all;
	entity nodo_2 is
		generic(
			N : natural := 32;
			N_SEM : natural := 10;
			N_MDC : natural := 2;
			N_CVS : natural := 10
		);
		port(
			Clock :  in std_logic;
			Reset :  in std_logic;
			Estado_i :  in std_logic;
			Estado_ante :  in std_logic;
			Estado_post :  in std_logic;
			Estado_o :  out std_logic
		);
	end entity nodo_2;
architecture Behavioral of nodo_2 is
begin
	Estado_o <= Estado_i;
end Behavioral;