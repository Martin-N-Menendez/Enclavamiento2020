-- paquete_pkg.vhdl : Achivo VHDL generado automaticamente
library IEEE;
use IEEE.std_logic_1164.all;
use IEEE.numeric_std.all;
	package my_package is
		type sems_type is record
			msb : std_logic_vector(10-1 downto 0);
			lsb : std_logic_vector(10-1 downto 0);
		end record sems_type;
		type sem_type is record
			msb : std_logic;
			lsb : std_logic;
		end record sem_type;
		type int_array is array(0 to 10-1) of integer;
	end my_package;
