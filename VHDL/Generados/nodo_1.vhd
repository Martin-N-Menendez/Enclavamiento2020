-- nodo_1.vhdl : Achivo VHDL generado automaticamente por el generador de código RAILIB
library IEEE;
use IEEE.std_logic_1164.all;
use IEEE.numeric_std.all;
--entidad_1 de nodo
entity nodo_1 is
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
end entity nodo_1;
-- Arquitectura de FSM_cambios_1 : Descripcion del comportamiento
architecture nodo_1_ARQ of nodo_1 is
	begin
end architecture nodo_1_ARQ;
