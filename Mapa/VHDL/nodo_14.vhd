-- nodo_14.vhdl : Achivo VHDL generado automaticamente
library IEEE;
use IEEE.std_logic_1164.all;
use IEEE.numeric_std.all;
--Declare the package
use work.my_package.all;
	entity nodo_14 is
		generic(
			N : natural := 90;
			N_SEM : natural := 27;
			N_MDC : natural := 12;
			N_CVS : natural := 24
		);
		port(
			Clock :  in std_logic;
			Reset :  in std_logic;
			Estado_i :  in std_logic;
			Estado_ante :  in std_logic;
			Estado_post :  in std_logic;
			Estado_o :  out std_logic
		);
	end entity nodo_14;
architecture Behavioral of nodo_14 is
begin
	Estado_o <= Estado_i;
end Behavioral;