-- nodo_3.vhdl : Achivo VHDL generado automaticamente por el generador de código RAILIB
library IEEE;
use IEEE.std_logic_1164.all;
use IEEE.numeric_std.all;
--entidad_3 de nodo
entity nodo_3 is
	generic(
		N_RUT : natural := 3;
		N_SEM : natural := 3
	);
	port(
		Clock : in std_logic;
		Reset : in std_logic;
		Anterior : in std_logic;
		Desvio : in std_logic;
		Posterior : out std_logic
	);
end entity nodo_3;
-- Arquitectura de FSM_cambios_3 : Descripcion del comportamiento
architecture nodo_3_ARQ of nodo_3 is
	begin
end architecture nodo_3_ARQ;
