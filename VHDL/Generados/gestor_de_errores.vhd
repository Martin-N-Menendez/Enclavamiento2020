-- gestor_de_errores.vhdl : Achivo VHDL generado automaticamente por el generador de código RAILIB
library IEEE;
use IEEE.std_logic_1164.all;
use IEEE.numeric_std.all;
--entidad de conector
entity conector is
	generic(
		N_CVS : natural := 2
	);
	port(
		Clock : in std_logic;
		Error_1 : in std_logic;
		Error_2 : in std_logic;
		Error : out std_logic_vector(N_CVS-1 downto 0)
	);
end entity conector;
-- Arquitectura del validador_modo : Descripcion del comportamiento
architecture gestor_de_errores_ARQ of gestor_de_errores is
	begin
