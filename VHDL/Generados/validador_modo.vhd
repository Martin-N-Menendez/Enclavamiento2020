-- validador_modo.vhdl : Achivo VHDL generado automaticamente por el generador de código RAILIB
library IEEE;
use IEEE.std_logic_1164.all;
use IEEE.numeric_std.all;
--entidad de nodo
entity nodo is
	generic(
		N_CVS : natural := 2;
		N_RUT : natural := 2
	);
	port(
		Clock : in std_logic;
		Modo_in : in std_logic_vector(N_RUT-1 downto 0);
		Modo_out : out std_logic_vector(N_RUT-1 downto 0)
	);
end entity nodo;
-- Arquitectura del validador_modo : Descripcion del comportamiento
architecture validador_modo_ARQ of validador_modo is
	begin
	process(Clock)
	begin
		if (Clock ='1' and Clock'Event) then
			Modo_out <= Modo_in;
		end if;
	end process;
end architecture validador_modo_ARQ;
