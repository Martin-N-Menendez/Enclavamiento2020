-- red.vhdl : Achivo VHDL generado automaticamente
library IEEE;
use IEEE.std_logic_1164.all;
use IEEE.numeric_std.all;
--Declare the package
use work.my_package.all;
	entity red is
		generic(
			N : natural := 21;
			N_SEM : natural := 7;
			N_MDC : natural := 1;
			N_CVS : natural := 6
		);
		port(
			Clock :  in std_logic;
			procesar :  in std_logic;
			procesado :  out std_logic;
			Ocupacion :  in std_logic_vector(N_CVS-1 downto 0);
			semaforos_i :  in sems_type;
			semaforos_o :  out sems_type;
			Cambios_i :  in std_logic;
			Cambios_o :  out std_logic;
			Reset :  in std_logic
		);
	end entity red;
architecture Behavioral of red is
	component cambio_1 is
		generic(
			N : natural := 21;
			N_SEM : natural := 7;
			N_MDC : natural := 1;
			N_CVS : natural := 6
		);
		port(
			Clock :  in std_logic;
			Estado_ante_i :  in std_logic;
			Estado_post_i :  in std_logic;
			Estado_desv_i :  in std_logic;
			Estado_ante_o :  out std_logic;
			Estado_post_o :  out std_logic;
			Estado_desv_o :  out std_logic;
			Cambio_i :  in std_logic;
			Cambio_o :  out std_logic;
			Reset :  in std_logic
		);
	end component cambio_1;
	component nodo_1 is
		generic(
			N : natural := 21;
			N_SEM : natural := 7;
			N_MDC : natural := 1;
			N_CVS : natural := 6
		);
		port(
			Clock :  in std_logic;
			Reset :  in std_logic;
			Estado_i :  in std_logic;
			Estado_post :  in std_logic;
			Semaforo_propio_i_1 :  in sem_type;
			Semaforo_propio_o_1 :  out sem_type;
			Semaforo_cercano :  out sem_type;
			Estado_o :  out std_logic
		);
	end component nodo_1;
	component nodo_2 is
		generic(
			N : natural := 21;
			N_SEM : natural := 7;
			N_MDC : natural := 1;
			N_CVS : natural := 6
		);
		port(
			Clock :  in std_logic;
			Reset :  in std_logic;
			Estado_i :  in std_logic;
			Estado_ante :  in std_logic;
			Estado_post :  in std_logic;
			Semaforo_propio_i_1 :  in sem_type;
			Semaforo_propio_o_1 :  out sem_type;
			Semaforo_propio_i_2 :  in sem_type;
			Semaforo_propio_o_2 :  out sem_type;
			Semaforo_propio_i_3 :  in sem_type;
			Semaforo_propio_o_3 :  out sem_type;
			Estado_o :  out std_logic
		);
	end component nodo_2;
	component nodo_3 is
		generic(
			N : natural := 21;
			N_SEM : natural := 7;
			N_MDC : natural := 1;
			N_CVS : natural := 6
		);
		port(
			Clock :  in std_logic;
			Reset :  in std_logic;
			Estado_i :  in std_logic;
			Estado_ante :  in std_logic;
			Estado_post :  in std_logic;
			Estado_o :  out std_logic
		);
	end component nodo_3;
	component nodo_4 is
		generic(
			N : natural := 21;
			N_SEM : natural := 7;
			N_MDC : natural := 1;
			N_CVS : natural := 6
		);
		port(
			Clock :  in std_logic;
			Reset :  in std_logic;
			Estado_i :  in std_logic;
			Estado_ante :  in std_logic;
			Estado_post :  in std_logic;
			Semaforo_propio_i_1 :  in sem_type;
			Semaforo_propio_o_1 :  out sem_type;
			Estado_o :  out std_logic
		);
	end component nodo_4;
	component nodo_5 is
		generic(
			N : natural := 21;
			N_SEM : natural := 7;
			N_MDC : natural := 1;
			N_CVS : natural := 6
		);
		port(
			Clock :  in std_logic;
			Reset :  in std_logic;
			Estado_i :  in std_logic;
			Estado_ante :  in std_logic;
			Semaforo_propio_i_1 :  in sem_type;
			Semaforo_propio_o_1 :  out sem_type;
			Semaforo_cercano :  out sem_type;
			Estado_o :  out std_logic
		);
	end component nodo_5;
	component nodo_6 is
		generic(
			N : natural := 21;
			N_SEM : natural := 7;
			N_MDC : natural := 1;
			N_CVS : natural := 6
		);
		port(
			Clock :  in std_logic;
			Reset :  in std_logic;
			Estado_i :  in std_logic;
			Estado_ante :  in std_logic;
			Semaforo_propio_i_1 :  in sem_type;
			Semaforo_propio_o_1 :  out sem_type;
			Semaforo_cercano :  out sem_type;
			Estado_o :  out std_logic
		);
	end component nodo_6;
	Signal conector_1 : std_logic;
	Signal ocupacion_1 : std_logic;
	Signal conector_2 : std_logic;
	Signal ocupacion_2 : std_logic;
	Signal conector_3 : std_logic;
	Signal ocupacion_3 : std_logic;
	Signal conector_4 : std_logic;
	Signal ocupacion_4 : std_logic;
	Signal conector_5 : std_logic;
	Signal ocupacion_5 : std_logic;
	Signal conector_6 : std_logic;
	Signal ocupacion_6 : std_logic;
	Signal sem_lsb_i_1 : std_logic;
	Signal sem_msb_i_1 : std_logic;
	Signal sem_lsb_o_1 : std_logic;
	Signal sem_msb_o_1 : std_logic;
	Signal sem_lsb_i_2 : std_logic;
	Signal sem_msb_i_2 : std_logic;
	Signal sem_lsb_o_2 : std_logic;
	Signal sem_msb_o_2 : std_logic;
	Signal sem_lsb_i_3 : std_logic;
	Signal sem_msb_i_3 : std_logic;
	Signal sem_lsb_o_3 : std_logic;
	Signal sem_msb_o_3 : std_logic;
	Signal sem_lsb_i_4 : std_logic;
	Signal sem_msb_i_4 : std_logic;
	Signal sem_lsb_o_4 : std_logic;
	Signal sem_msb_o_4 : std_logic;
	Signal sem_lsb_i_5 : std_logic;
	Signal sem_msb_i_5 : std_logic;
	Signal sem_lsb_o_5 : std_logic;
	Signal sem_msb_o_5 : std_logic;
	Signal sem_lsb_i_6 : std_logic;
	Signal sem_msb_i_6 : std_logic;
	Signal sem_lsb_o_6 : std_logic;
	Signal sem_msb_o_6 : std_logic;
	Signal sem_lsb_i_7 : std_logic;
	Signal sem_msb_i_7 : std_logic;
	Signal sem_lsb_o_7 : std_logic;
	Signal sem_msb_o_7 : std_logic;
	Signal mdc_i_1 : std_logic;
	Signal mdc_o_1 : std_logic;
	Signal mdc_ante_i_1 : std_logic;
	Signal mdc_ante_o_1 : std_logic;
	Signal mdc_post_i_1 : std_logic;
	Signal mdc_post_o_1 : std_logic;
	Signal mdc_desv_i_1 : std_logic;
	Signal mdc_desv_o_1 : std_logic;
	Signal cosa : std_logic;
begin
	nodo_1_i:nodo_1 port map(
		Clock => Clock,
		Estado_post => conector_2,
		Semaforo_propio_i_1.lsb => sem_lsb_i_1,
		Semaforo_propio_i_1.msb => sem_msb_i_1,
		Semaforo_propio_o_1.lsb => sem_lsb_o_1,
		Semaforo_propio_o_1.msb => sem_msb_o_1,
		Semaforo_cercano.lsb => cosa,
		Semaforo_cercano.msb => cosa,
		Estado_i => ocupacion_1,
		Estado_o => conector_1,
		Reset => Reset
		);
	nodo_2_i:nodo_2 port map(
		Clock => Clock,
		Estado_ante => conector_1,
		Estado_post => mdc_ante_o_1,
		Semaforo_propio_i_1.lsb => sem_lsb_i_2,
		Semaforo_propio_i_1.msb => sem_msb_i_2,
		Semaforo_propio_o_1.lsb => sem_lsb_o_2,
		Semaforo_propio_o_1.msb => sem_msb_o_2,
		Semaforo_propio_i_2.lsb => sem_lsb_i_3,
		Semaforo_propio_i_2.msb => sem_msb_i_3,
		Semaforo_propio_o_2.lsb => sem_lsb_o_3,
		Semaforo_propio_o_2.msb => sem_msb_o_3,
		Semaforo_propio_i_3.lsb => sem_lsb_i_4,
		Semaforo_propio_i_3.msb => sem_msb_i_4,
		Semaforo_propio_o_3.lsb => sem_lsb_o_4,
		Semaforo_propio_o_3.msb => sem_msb_o_4,
		Estado_i => ocupacion_2,
		Estado_o => conector_2,
		Reset => Reset
		);
	nodo_3_i:nodo_3 port map(
		Clock => Clock,
		Estado_ante => mdc_post_o_1,
		Estado_post => conector_5,
		Estado_i => ocupacion_3,
		Estado_o => conector_3,
		Reset => Reset
		);
	nodo_4_i:nodo_4 port map(
		Clock => Clock,
		Estado_ante => mdc_desv_o_1,
		Estado_post => conector_6,
		Semaforo_propio_i_1.lsb => sem_lsb_i_5,
		Semaforo_propio_i_1.msb => sem_msb_i_5,
		Semaforo_propio_o_1.lsb => sem_lsb_o_5,
		Semaforo_propio_o_1.msb => sem_msb_o_5,
		Estado_i => ocupacion_4,
		Estado_o => conector_4,
		Reset => Reset
		);
	nodo_5_i:nodo_5 port map(
		Clock => Clock,
		Estado_ante => conector_3,
		Semaforo_propio_i_1.lsb => sem_lsb_i_6,
		Semaforo_propio_i_1.msb => sem_msb_i_6,
		Semaforo_propio_o_1.lsb => sem_lsb_o_6,
		Semaforo_propio_o_1.msb => sem_msb_o_6,
		Semaforo_cercano.lsb => cosa,
		Semaforo_cercano.msb => cosa,
		Estado_i => ocupacion_5,
		Estado_o => conector_5,
		Reset => Reset
		);
	nodo_6_i:nodo_6 port map(
		Clock => Clock,
		Estado_ante => conector_4,
		Semaforo_propio_i_1.lsb => sem_lsb_i_7,
		Semaforo_propio_i_1.msb => sem_msb_i_7,
		Semaforo_propio_o_1.lsb => sem_lsb_o_7,
		Semaforo_propio_o_1.msb => sem_msb_o_7,
		Semaforo_cercano.lsb => cosa,
		Semaforo_cercano.msb => cosa,
		Estado_i => ocupacion_6,
		Estado_o => conector_6,
		Reset => Reset
		);
	cambio_1_i:cambio_1 port map(
		Clock => Clock,
		Cambio_i => mdc_i_1,
		Cambio_o => mdc_o_1,
		Estado_ante_i => conector_2,
		Estado_ante_o => mdc_ante_o_1,
		Estado_post_i => conector_3,
		Estado_post_o => mdc_post_o_1,
		Estado_desv_i => conector_4,
		Estado_desv_o => mdc_desv_o_1,
		Reset => Reset
		);
		cosa <= '0';
		ocupacion_1 <= Ocupacion(0);
		ocupacion_2 <= Ocupacion(1);
		ocupacion_3 <= Ocupacion(2);
		ocupacion_4 <= Ocupacion(3);
		ocupacion_5 <= Ocupacion(4);
		ocupacion_6 <= Ocupacion(5);
		mdc_i_1 <= Cambios_i;
		Cambios_o <= mdc_o_1;
		sem_lsb_i_1 <= semaforos_i.lsb(0);
		sem_msb_i_1 <= semaforos_i.msb(0);
		semaforos_o.lsb(0) <= sem_lsb_o_1;
		semaforos_o.msb(0) <= sem_msb_o_1;
		sem_lsb_i_2 <= semaforos_i.lsb(1);
		sem_msb_i_2 <= semaforos_i.msb(1);
		semaforos_o.lsb(1) <= sem_lsb_o_2;
		semaforos_o.msb(1) <= sem_msb_o_2;
		sem_lsb_i_3 <= semaforos_i.lsb(2);
		sem_msb_i_3 <= semaforos_i.msb(2);
		semaforos_o.lsb(2) <= sem_lsb_o_3;
		semaforos_o.msb(2) <= sem_msb_o_3;
		sem_lsb_i_4 <= semaforos_i.lsb(3);
		sem_msb_i_4 <= semaforos_i.msb(3);
		semaforos_o.lsb(3) <= sem_lsb_o_4;
		semaforos_o.msb(3) <= sem_msb_o_4;
		sem_lsb_i_5 <= semaforos_i.lsb(4);
		sem_msb_i_5 <= semaforos_i.msb(4);
		semaforos_o.lsb(4) <= sem_lsb_o_5;
		semaforos_o.msb(4) <= sem_msb_o_5;
		sem_lsb_i_6 <= semaforos_i.lsb(5);
		sem_msb_i_6 <= semaforos_i.msb(5);
		semaforos_o.lsb(5) <= sem_lsb_o_6;
		semaforos_o.msb(5) <= sem_msb_o_6;
		sem_lsb_i_7 <= semaforos_i.lsb(6);
		sem_msb_i_7 <= semaforos_i.msb(6);
		semaforos_o.lsb(6) <= sem_lsb_o_7;
		semaforos_o.msb(6) <= sem_msb_o_7;
		procesado <= procesar;
end Behavioral;