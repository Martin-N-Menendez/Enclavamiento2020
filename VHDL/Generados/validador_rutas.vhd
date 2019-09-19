-- validador_rutas.vhdl : Achivo VHDL generado automaticamente por el generador de código RAILIB
library IEEE;
use IEEE.std_logic_1164.all;
use IEEE.numeric_std.all;
--entidad de conector
entity conector is
	generic(
		N_CVS : natural := 2;
		N_RUT : natural := 2
	);
	port(
		Clock : in std_logic;
		Modo_in : in std_logic_vector(N_RUT-1 downto 0);
		Ruta_in : in std_logic_vector(N_RUT-1 downto 0);
		Ocupacion : in std_logic_vector(N_CVS-1 downto 0);
		Rutas_out : out std_logic_vector(N_RUT-1 downto 0)
	);
end entity conector;
-- Arquitectura del validador_modo : Descripcion del comportamiento
architecture validador_rutas_ARQ of validador_rutas is
	begin
	process(Clock)
	begin
		if (Clock ='1' and Clock'Event) then
			Rutas_out <= Ruta_in;
		end if;
	end process;
end architecture validador_rutas_ARQ;
