-- nodo_2.vhdl : Achivo VHDL generado automaticamente por el generador de código RAILIB
library IEEE;
use IEEE.std_logic_1164.all;
use IEEE.numeric_std.all;
--entidad_2 de nodo
entity nodo_2 is
	generic(
		N_RUT : natural := 5;
		N_SEM : natural := 5
	);
	port(
		Clock : in std_logic;
		Reset : in std_logic;
		Anterior : in std_logic;
		Desvio : in std_logic;
		Posterior : out std_logic
	);
end entity nodo_2;
-- Arquitectura de FSM_cambios_2 : Descripcion del comportamiento
architecture nodo_2_ARQ of nodo_2 is
	begin
end architecture nodo_2_ARQ;
