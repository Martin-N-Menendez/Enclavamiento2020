-- capa_logica.vhdl : Achivo VHDL generado automaticamente por el generador de código RAILIB
library IEEE;
use IEEE.std_logic_1164.all;
use IEEE.numeric_std.all;
--entidad de capa_logica
entity capa_logica is
	generic(
		N_CVS : natural := 3;
		N_SEM : natural := 3;
		N_PAN : natural := 1;
		N_MDC : natural := 2;
		N_RUT : natural := 3
	);
	port(
		Clock : in std_logic;
		Reset : in std_logic;
		Modo : in std_logic_vector(N_RUT-1 downto 0);
		Ruta_in : in std_logic_vector(N_RUT-1 downto 0);
		Circuitos_de_via : in std_logic_vector(N_CVS-1 downto 0);
		Semaforo_out : out std_logic_vector(N_SEM-1 downto 0);
		Barrera_out : out std_logic_vector(N_PAN-1 downto 0);
		Maquina_out : out std_logic_vector(N_MDC-1 downto 0)
	);
end entity capa_logica;
-- Arquitectura de la capa_logica: Descripcion del comportamiento
architecture capa_logica_ARQ of capa_logica is
	--componente_1 de nodo
	component nodo_1 is
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
	end component nodo_1;
	--componente_2 de nodo
	component nodo_2 is
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
	end component nodo_2;
	--componente_3 de nodo
	component nodo_3 is
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
	end component nodo_3;
	Signal conector_1a2 , conector_2a3 : std_logic;
	begin
	nodo_inst_1:nodo_1
		port map(
			Clock => Clock,
			Anterior => Clock,
			Desvio => Clock,
			Reset => Reset
		);
	nodo_inst_2:nodo_2
		port map(
			Clock => Clock,
			Anterior => Clock,
			Desvio => Clock,
			Reset => Reset
		);
	nodo_inst_3:nodo_3
		port map(
			Clock => Clock,
: natural := 5;
			N_SEM : natural := 5
		);
		port(
			Clock : in std_logic;
			Reset : in std_logic;
			Anterior : in std_logic;
			Desvio : in std_logic;
			Posterior : out std_logic
		);
	end component nodo_5;
	Signal conector_0a1 , conector_1a2 , conector_2a4 , conector_3a3 : std_logic;
	Signal wires : std_logic_vector(10 downto 0);
	begin
	wires(0) <= Clock;
	nodo_inst_1:nodo_1
		port map(
			Clock => Clock,
			Posterior => wires(1),
			Anterior => wires(0),
			Desvio => Clock,
			Reset => Reset
		);
	nodo_inst_2:nodo_2
		port map(
			Clock => Clock,
			Anterior => wires(1),
			Posterior => wires(2),
			Desvio => Clock,
			Reset => Reset
		);
	nodo_inst_3:nodo_3
		port map(
			Clock => Clock,
			Anterior => wires(2),
			Posterior => wires(3),
			Desvio => Clock,
			Reset => Reset
		);
	nodo_inst_4:nodo_4
		port map(
			Clock => Clock,
			Posterior => wires(4),
			Anterior => wires(3),
			Desvio => Clock,
			Reset => Reset
		);
	nodo_inst_5:nodo_5
		port map(
			Clock => Clock,
			Anterior => wires(4),
			Desvio => Clock,
			Reset => Reset
		);
end architecture capa_logica_ARQ;
