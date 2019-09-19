-- senialamiento.vhdl : Achivo VHDL generado automaticamente por el generador de código RAILIB
library IEEE;
use IEEE.std_logic_1164.all;
use IEEE.numeric_std.all;
--entidad de senialamiento
entity senialamiento is
	generic(
		N_CVS : natural := 3;
		N_SEM : natural := 3;
		N_PAN : natural := 1;
		N_MDC : natural := 2
	);
	port(
		Clock : in std_logic;
		Reset : in std_logic;
		Semaforo_rojo_in : in std_logic_vector(N_SEM-1 downto 0);
		Semaforo_amarillo_in : in std_logic_vector(N_SEM-1 downto 0);
		Semaforo_verde_in : in std_logic_vector(N_SEM-1 downto 0);
		Barrera_alta_in : in std_logic_vector(N_PAN-1 downto 0);
		Barrera_baja_in : in std_logic_vector(N_PAN-1 downto 0);
		Maquina_normal_in : in std_logic_vector(N_MDC-1 downto 0);
		Maquina_reversa_in : in std_logic_vector(N_MDC-1 downto 0);
		Semaforo_rojo_out : out std_logic_vector(N_SEM-1 downto 0);
		Semaforo_amarillo_out : out std_logic_vector(N_SEM-1 downto 0);
		Semaforo_verde_out : out std_logic_vector(N_SEM-1 downto 0);
		Barrera_alta_out : out std_logic_vector(N_PAN-1 downto 0);
		Barrera_baja_out : out std_logic_vector(N_PAN-1 downto 0);
		Maquina_normal_out : out std_logic_vector(N_MDC-1 downto 0);
		Maquina_reversa_out : out std_logic_vector(N_MDC-1 downto 0)
	);
end entity senialamiento;
-- Arquitectura del señalamiento : Descripcion del comportamiento
architecture senialamiento_ARQ of senialamiento is
	--componente de semaforos
	component semaforos is
		port(
			Clock : in std_logic;
			Reset : in std_logic;
			Rojo_in : in std_logic_vector(N_SEM-1 downto 0);
			Amarillo_in : in std_logic_vector(N_SEM-1 downto 0);
			Verde_in : in std_logic_vector(N_SEM-1 downto 0);
			Rojo_out : out std_logic_vector(N_SEM-1 downto 0);
			Amarillo_out : out std_logic_vector(N_SEM-1 downto 0);
			Verde_out : out std_logic_vector(N_SEM-1 downto 0)
		);
	end component semaforos;
	--componente de pasos_a_nivel
	component pasos_a_nivel is
		port(
			Clock : in std_logic;
			Reset : in std_logic;
			Alto_in : in std_logic_vector(N_PAN-1 downto 0);
			Bajo_in : in std_logic_vector(N_PAN-1 downto 0);
			Alto_out : out std_logic_vector(N_PAN-1 downto 0);
			Bajo_out : out std_logic_vector(N_PAN-1 downto 0)
		);
	end component pasos_a_nivel;
	--componente de cambios
	component cambios is
		port(
			Clock : in std_logic;
			Reset : in std_logic;
			Maquina_normal_in : in std_logic_vector(N_MDC-1 downto 0);
			Maquina_reversa_in : in std_logic_vector(N_MDC-1 downto 0);
			Maquina_normal_out : out std_logic_vector(N_MDC-1 downto 0);
			Maquina_reversa_out : out std_logic_vector(N_MDC-1 downto 0)
		);
	end component cambios;
	Signal Rojo_in_s,Amarillo_in_s,Verde_in_s,Rojo_out_s,Amarillo_out_s,Verde_out_s: std_logic_vector(N_SEM-1 downto 0);
	Signal Alto_in_s,Bajo_in_s,Alto_out_s,Bajo_out_s: std_logic_vector(N_PAN-1 downto 0);
	Signal Maquina_normal_in_s,Maquina_reversa_in_s,Maquina_normal_out_s,Maquina_reversa_out_s: std_logic_vector(N_MDC-1 downto 0);
	Signal Reset_sem_s,Reset_Pan_s: std_logic;
	begin
	semaforo_inst : semaforos port map(
		Clock => Clock,
		Reset => Reset,
		Rojo_in => Rojo_in_s,
		Amarillo_in => Amarillo_in_s,
		Verde_in => Verde_in_s,
		Rojo_out => Rojo_out_s,
		Amarillo_out => Amarillo_out_s,
		Verde_out => Verde_out_s);
	paso_a_nivel_inst:pasos_a_nivel port map(
		Clock => Clock,
		Reset => Reset,
		Alto_in => Alto_in_s,
		Bajo_in => Bajo_in_s,
		Alto_out => Alto_out_s,
		Bajo_out => Bajo_out_s);
	cambio_inst:cambios port map(
		Clock => Clock,
		Reset => Reset,
		Maquina_normal_in => Maquina_normal_in_s,
		Maquina_reversa_in => Maquina_reversa_in_s,
		Maquina_normal_out => Maquina_normal_out_s,
		Maquina_reversa_out => Maquina_reversa_out_s);
	Rojo_in_s <= Semaforo_rojo_in;
	Amarillo_in_s <= Semaforo_amarillo_in;
	Verde_in_s <= Semaforo_verde_in;
	Semaforo_rojo_out <= Rojo_out_s;
	Semaforo_amarillo_out <= Amarillo_out_s;
	Semaforo_verde_out <= Verde_out_s;
	Alto_in_s <= Barrera_alta_in;
	Bajo_in_s <= Barrera_baja_in;
	Barrera_alta_out <= Alto_out_s;
	Barrera_baja_out <= Bajo_out_s;
	Maquina_normal_in_s <= Maquina_normal_in;
	Maquina_reversa_in_s <= Maquina_reversa_in;
	Maquina_normal_out <= Maquina_normal_out_s;
	Maquina_reversa_out <= Maquina_reversa_out_s;
	process(Clock,Reset)
	begin
		if (Clock ='1' and Clock'Event and Reset='1') then
			Reset_sem_s <= '0';
			Reset_pan_s <= '0';
		end if;
	end process;
end architecture senialamiento_ARQ;
