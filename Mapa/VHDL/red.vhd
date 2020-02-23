-- red.vhdl : Achivo VHDL generado automaticamente
library IEEE;
use IEEE.std_logic_1164.all;
use IEEE.numeric_std.all;
--Declare the package
use work.my_package.all;
	entity red is
		generic(
			N : natural := 119;
			N_SEM : natural := 36;
			N_MDC : natural := 14;
			N_CVS : natural := 33
		);
		port(
			Clock :  in std_logic;
			Ocupacion :  in std_logic_vector(N_CVS-1 downto 0);
			semaforos_i :  in sems_type;
			semaforos_o :  out sems_type;
			Cambios_i :  in std_logic_vector(N_MDC-1 downto 0);
			Cambios_o :  out std_logic_vector(N_MDC-1 downto 0);
			Reset :  in std_logic
		);
	end entity red;
architecture Behavioral of red is
	component cambio_1 is
		generic(
			N : natural := 119;
			N_SEM : natural := 36;
			N_MDC : natural := 14;
			N_CVS : natural := 33
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
			Reset :  in std_logic;
		);
	end component cambio_1;
	component cambio_2 is
		generic(
			N : natural := 119;
			N_SEM : natural := 36;
			N_MDC : natural := 14;
			N_CVS : natural := 33
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
			Reset :  in std_logic;
		);
	end component cambio_2;
	component cambio_3 is
		generic(
			N : natural := 119;
			N_SEM : natural := 36;
			N_MDC : natural := 14;
			N_CVS : natural := 33
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
			Reset :  in std_logic;
		);
	end component cambio_3;
	component cambio_4 is
		generic(
			N : natural := 119;
			N_SEM : natural := 36;
			N_MDC : natural := 14;
			N_CVS : natural := 33
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
			Reset :  in std_logic;
		);
	end component cambio_4;
	component cambio_5 is
		generic(
			N : natural := 119;
			N_SEM : natural := 36;
			N_MDC : natural := 14;
			N_CVS : natural := 33
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
			Reset :  in std_logic;
		);
	end component cambio_5;
	component cambio_6 is
		generic(
			N : natural := 119;
			N_SEM : natural := 36;
			N_MDC : natural := 14;
			N_CVS : natural := 33
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
			Reset :  in std_logic;
		);
	end component cambio_6;
	component cambio_7 is
		generic(
			N : natural := 119;
			N_SEM : natural := 36;
			N_MDC : natural := 14;
			N_CVS : natural := 33
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
			Reset :  in std_logic;
		);
	end component cambio_7;
	component cambio_8 is
		generic(
			N : natural := 119;
			N_SEM : natural := 36;
			N_MDC : natural := 14;
			N_CVS : natural := 33
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
			Reset :  in std_logic;
		);
	end component cambio_8;
	component cambio_9 is
		generic(
			N : natural := 119;
			N_SEM : natural := 36;
			N_MDC : natural := 14;
			N_CVS : natural := 33
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
			Reset :  in std_logic;
		);
	end component cambio_9;
	component cambio_10 is
		generic(
			N : natural := 119;
			N_SEM : natural := 36;
			N_MDC : natural := 14;
			N_CVS : natural := 33
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
			Reset :  in std_logic;
		);
	end component cambio_10;
	component cambio_11 is
		generic(
			N : natural := 119;
			N_SEM : natural := 36;
			N_MDC : natural := 14;
			N_CVS : natural := 33
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
			Reset :  in std_logic;
		);
	end component cambio_11;
	component cambio_12 is
		generic(
			N : natural := 119;
			N_SEM : natural := 36;
			N_MDC : natural := 14;
			N_CVS : natural := 33
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
			Reset :  in std_logic;
		);
	end component cambio_12;
	component cambio_13 is
		generic(
			N : natural := 119;
			N_SEM : natural := 36;
			N_MDC : natural := 14;
			N_CVS : natural := 33
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
			Reset :  in std_logic;
		);
	end component cambio_13;
	component cambio_14 is
		generic(
			N : natural := 119;
			N_SEM : natural := 36;
			N_MDC : natural := 14;
			N_CVS : natural := 33
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
			Reset :  in std_logic;
		);
	end component cambio_14;
	component nodo_1 is
		generic(
			N : natural := 119;
			N_SEM : natural := 36;
			N_MDC : natural := 14;
			N_CVS : natural := 33
		);
		port(
			Clock :  in std_logic;
			Reset :  in std_logic;
			Estado_i :  in std_logic;
			Estado_post :  out std_logic;
			Semaforo_propio_i_1 :  in sem_type;
			Semaforo_propio_o_1 :  out sem_type;
			Semaforo_cercano :  out sem_type;
			Estado_o :  out std_logic
		);
	end component nodo_1;
	component nodo_2 is
		generic(
			N : natural := 119;
			N_SEM : natural := 36;
			N_MDC : natural := 14;
			N_CVS : natural := 33
		);
		port(
			Clock :  in std_logic;
			Reset :  in std_logic;
			Estado_i :  in std_logic;
			Estado_ante :  out std_logic;
			Estado_post :  out std_logic;
			Semaforo_propio_i_1 :  in sem_type;
			Semaforo_propio_o_1 :  out sem_type;
			Semaforo_propio_i_2 :  in sem_type;
			Semaforo_propio_o_2 :  out sem_type;
			Estado_o :  out std_logic
		);
	end component nodo_2;
	component nodo_3 is
		generic(
			N : natural := 119;
			N_SEM : natural := 36;
			N_MDC : natural := 14;
			N_CVS : natural := 33
		);
		port(
			Clock :  in std_logic;
			Reset :  in std_logic;
			Estado_i :  in std_logic;
			Estado_ante :  out std_logic;
			Estado_post :  out std_logic;
			Semaforo_propio_i_1 :  in sem_type;
			Semaforo_propio_o_1 :  out sem_type;
			Estado_o :  out std_logic
		);
	end component nodo_3;
	component nodo_4 is
		generic(
			N : natural := 119;
			N_SEM : natural := 36;
			N_MDC : natural := 14;
			N_CVS : natural := 33
		);
		port(
			Clock :  in std_logic;
			Reset :  in std_logic;
			Estado_i :  in std_logic;
			Estado_ante :  out std_logic;
			Estado_post :  out std_logic;
			Semaforo_propio_i_1 :  in sem_type;
			Semaforo_propio_o_1 :  out sem_type;
			Semaforo_propio_i_2 :  in sem_type;
			Semaforo_propio_o_2 :  out sem_type;
			Semaforo_propio_i_3 :  in sem_type;
			Semaforo_propio_o_3 :  out sem_type;
			Semaforo_cercano :  out sem_type;
			Estado_o :  out std_logic
		);
	end component nodo_4;
	component nodo_5 is
		generic(
			N : natural := 119;
			N_SEM : natural := 36;
			N_MDC : natural := 14;
			N_CVS : natural := 33
		);
		port(
			Clock :  in std_logic;
			Reset :  in std_logic;
			Estado_i :  in std_logic;
			Estado_ante :  out std_logic;
			Estado_post :  out std_logic;
			Estado_o :  out std_logic
		);
	end component nodo_5;
	component nodo_6 is
		generic(
			N : natural := 119;
			N_SEM : natural := 36;
			N_MDC : natural := 14;
			N_CVS : natural := 33
		);
		port(
			Clock :  in std_logic;
			Reset :  in std_logic;
			Estado_i :  in std_logic;
			Estado_ante :  out std_logic;
			Estado_post :  out std_logic;
			Semaforo_propio_i_1 :  in sem_type;
			Semaforo_propio_o_1 :  out sem_type;
			Semaforo_propio_i_2 :  in sem_type;
			Semaforo_propio_o_2 :  out sem_type;
			Semaforo_cercano :  out sem_type;
			Estado_o :  out std_logic
		);
	end component nodo_6;
	component nodo_7 is
		generic(
			N : natural := 119;
			N_SEM : natural := 36;
			N_MDC : natural := 14;
			N_CVS : natural := 33
		);
		port(
			Clock :  in std_logic;
			Reset :  in std_logic;
			Estado_i :  in std_logic;
			Estado_ante :  out std_logic;
			Estado_post :  out std_logic;
			Estado_o :  out std_logic
		);
	end component nodo_7;
	component nodo_8 is
		generic(
			N : natural := 119;
			N_SEM : natural := 36;
			N_MDC : natural := 14;
			N_CVS : natural := 33
		);
		port(
			Clock :  in std_logic;
			Reset :  in std_logic;
			Estado_i :  in std_logic;
			Estado_ante :  out std_logic;
			Estado_post :  out std_logic;
			Estado_o :  out std_logic
		);
	end component nodo_8;
	component nodo_9 is
		generic(
			N : natural := 119;
			N_SEM : natural := 36;
			N_MDC : natural := 14;
			N_CVS : natural := 33
		);
		port(
			Clock :  in std_logic;
			Reset :  in std_logic;
			Estado_i :  in std_logic;
			Estado_ante :  out std_logic;
			Estado_post :  out std_logic;
			Semaforo_propio_i_1 :  in sem_type;
			Semaforo_propio_o_1 :  out sem_type;
			Semaforo_propio_i_2 :  in sem_type;
			Semaforo_propio_o_2 :  out sem_type;
			Semaforo_propio_i_3 :  in sem_type;
			Semaforo_propio_o_3 :  out sem_type;
			Estado_o :  out std_logic
		);
	end component nodo_9;
	component nodo_10 is
		generic(
			N : natural := 119;
			N_SEM : natural := 36;
			N_MDC : natural := 14;
			N_CVS : natural := 33
		);
		port(
			Clock :  in std_logic;
			Reset :  in std_logic;
			Estado_i :  in std_logic;
			Estado_ante :  out std_logic;
			Estado_post :  out std_logic;
			Semaforo_propio_i_1 :  in sem_type;
			Semaforo_propio_o_1 :  out sem_type;
			Semaforo_propio_i_2 :  in sem_type;
			Semaforo_propio_o_2 :  out sem_type;
			Semaforo_propio_i_3 :  in sem_type;
			Semaforo_propio_o_3 :  out sem_type;
			Semaforo_cercano :  out sem_type;
			Estado_o :  out std_logic
		);
	end component nodo_10;
	component nodo_11 is
		generic(
			N : natural := 119;
			N_SEM : natural := 36;
			N_MDC : natural := 14;
			N_CVS : natural := 33
		);
		port(
			Clock :  in std_logic;
			Reset :  in std_logic;
			Estado_i :  in std_logic;
			Estado_ante :  out std_logic;
			Estado_post :  out std_logic;
			Estado_o :  out std_logic
		);
	end component nodo_11;
	component nodo_12 is
		generic(
			N : natural := 119;
			N_SEM : natural := 36;
			N_MDC : natural := 14;
			N_CVS : natural := 33
		);
		port(
			Clock :  in std_logic;
			Reset :  in std_logic;
			Estado_i :  in std_logic;
			Estado_ante :  out std_logic;
			Estado_post :  out std_logic;
			Semaforo_propio_i_1 :  in sem_type;
			Semaforo_propio_o_1 :  out sem_type;
			Semaforo_propio_i_2 :  in sem_type;
			Semaforo_propio_o_2 :  out sem_type;
			Estado_o :  out std_logic
		);
	end component nodo_12;
	component nodo_13 is
		generic(
			N : natural := 119;
			N_SEM : natural := 36;
			N_MDC : natural := 14;
			N_CVS : natural := 33
		);
		port(
			Clock :  in std_logic;
			Reset :  in std_logic;
			Estado_i :  in std_logic;
			Estado_ante :  out std_logic;
			Estado_post :  out std_logic;
			Estado_o :  out std_logic
		);
	end component nodo_13;
	component nodo_14 is
		generic(
			N : natural := 119;
			N_SEM : natural := 36;
			N_MDC : natural := 14;
			N_CVS : natural := 33
		);
		port(
			Clock :  in std_logic;
			Reset :  in std_logic;
			Estado_i :  in std_logic;
			Estado_ante :  out std_logic;
			Estado_post :  out std_logic;
			Semaforo_propio_i_1 :  in sem_type;
			Semaforo_propio_o_1 :  out sem_type;
			Semaforo_propio_i_2 :  in sem_type;
			Semaforo_propio_o_2 :  out sem_type;
			Semaforo_cercano :  out sem_type;
			Estado_o :  out std_logic
		);
	end component nodo_14;
	component nodo_15 is
		generic(
			N : natural := 119;
			N_SEM : natural := 36;
			N_MDC : natural := 14;
			N_CVS : natural := 33
		);
		port(
			Clock :  in std_logic;
			Reset :  in std_logic;
			Estado_i :  in std_logic;
			Estado_ante :  out std_logic;
			Estado_post :  out std_logic;
			Semaforo_propio_i_1 :  in sem_type;
			Semaforo_propio_o_1 :  out sem_type;
			Semaforo_propio_i_2 :  in sem_type;
			Semaforo_propio_o_2 :  out sem_type;
			Semaforo_cercano :  out sem_type;
			Estado_o :  out std_logic
		);
	end component nodo_15;
	component nodo_16 is
		generic(
			N : natural := 119;
			N_SEM : natural := 36;
			N_MDC : natural := 14;
			N_CVS : natural := 33
		);
		port(
			Clock :  in std_logic;
			Reset :  in std_logic;
			Estado_i :  in std_logic;
			Estado_ante :  out std_logic;
			Estado_post :  out std_logic;
			Semaforo_propio_i_1 :  in sem_type;
			Semaforo_propio_o_1 :  out sem_type;
			Estado_o :  out std_logic
		);
	end component nodo_16;
	component nodo_17 is
		generic(
			N : natural := 119;
			N_SEM : natural := 36;
			N_MDC : natural := 14;
			N_CVS : natural := 33
		);
		port(
			Clock :  in std_logic;
			Reset :  in std_logic;
			Estado_i :  in std_logic;
			Estado_ante :  out std_logic;
			Estado_post :  out std_logic;
			Semaforo_propio_i_1 :  in sem_type;
			Semaforo_propio_o_1 :  out sem_type;
			Semaforo_propio_i_2 :  in sem_type;
			Semaforo_propio_o_2 :  out sem_type;
			Estado_o :  out std_logic
		);
	end component nodo_17;
	component nodo_18 is
		generic(
			N : natural := 119;
			N_SEM : natural := 36;
			N_MDC : natural := 14;
			N_CVS : natural := 33
		);
		port(
			Clock :  in std_logic;
			Reset :  in std_logic;
			Estado_i :  in std_logic;
			Estado_ante :  out std_logic;
			Estado_post :  out std_logic;
			Semaforo_propio_i_1 :  in sem_type;
			Semaforo_propio_o_1 :  out sem_type;
			Semaforo_propio_i_2 :  in sem_type;
			Semaforo_propio_o_2 :  out sem_type;
			Estado_o :  out std_logic
		);
	end component nodo_18;
	component nodo_19 is
		generic(
			N : natural := 119;
			N_SEM : natural := 36;
			N_MDC : natural := 14;
			N_CVS : natural := 33
		);
		port(
			Clock :  in std_logic;
			Reset :  in std_logic;
			Estado_i :  in std_logic;
			Estado_ante :  out std_logic;
			Semaforo_propio_i_1 :  in sem_type;
			Semaforo_propio_o_1 :  out sem_type;
			Semaforo_cercano :  out sem_type;
			Estado_o :  out std_logic
		);
	end component nodo_19;
	component nodo_20 is
		generic(
			N : natural := 119;
			N_SEM : natural := 36;
			N_MDC : natural := 14;
			N_CVS : natural := 33
		);
		port(
			Clock :  in std_logic;
			Reset :  in std_logic;
			Estado_i :  in std_logic;
			Estado_ante :  out std_logic;
			Semaforo_propio_i_1 :  in sem_type;
			Semaforo_propio_o_1 :  out sem_type;
			Semaforo_cercano :  out sem_type;
			Estado_o :  out std_logic
		);
	end component nodo_20;
	component nodo_21 is
		generic(
			N : natural := 119;
			N_SEM : natural := 36;
			N_MDC : natural := 14;
			N_CVS : natural := 33
		);
		port(
			Clock :  in std_logic;
			Reset :  in std_logic;
			Estado_i :  in std_logic;
			Estado_post :  out std_logic;
			Semaforo_propio_i_1 :  in sem_type;
			Semaforo_propio_o_1 :  out sem_type;
			Semaforo_cercano :  out sem_type;
			Estado_o :  out std_logic
		);
	end component nodo_21;
	component nodo_22 is
		generic(
			N : natural := 119;
			N_SEM : natural := 36;
			N_MDC : natural := 14;
			N_CVS : natural := 33
		);
		port(
			Clock :  in std_logic;
			Reset :  in std_logic;
			Estado_i :  in std_logic;
			Estado_ante :  out std_logic;
			Estado_post :  out std_logic;
			Semaforo_propio_i_1 :  in sem_type;
			Semaforo_propio_o_1 :  out sem_type;
			Semaforo_propio_i_2 :  in sem_type;
			Semaforo_propio_o_2 :  out sem_type;
			Estado_o :  out std_logic
		);
	end component nodo_22;
	component nodo_23 is
		generic(
			N : natural := 119;
			N_SEM : natural := 36;
			N_MDC : natural := 14;
			N_CVS : natural := 33
		);
		port(
			Clock :  in std_logic;
			Reset :  in std_logic;
			Estado_i :  in std_logic;
			Estado_ante :  out std_logic;
			Estado_post :  out std_logic;
			Semaforo_propio_i_1 :  in sem_type;
			Semaforo_propio_o_1 :  out sem_type;
			Semaforo_propio_i_2 :  in sem_type;
			Semaforo_propio_o_2 :  out sem_type;
			Semaforo_cercano :  out sem_type;
			Estado_o :  out std_logic
		);
	end component nodo_23;
	component nodo_24 is
		generic(
			N : natural := 119;
			N_SEM : natural := 36;
			N_MDC : natural := 14;
			N_CVS : natural := 33
		);
		port(
			Clock :  in std_logic;
			Reset :  in std_logic;
			Estado_i :  in std_logic;
			Estado_ante :  out std_logic;
			Estado_post :  out std_logic;
			Estado_o :  out std_logic
		);
	end component nodo_24;
	component nodo_25 is
		generic(
			N : natural := 119;
			N_SEM : natural := 36;
			N_MDC : natural := 14;
			N_CVS : natural := 33
		);
		port(
			Clock :  in std_logic;
			Reset :  in std_logic;
			Estado_i :  in std_logic;
			Estado_ante :  out std_logic;
			Estado_post :  out std_logic;
			Estado_o :  out std_logic
		);
	end component nodo_25;
	component nodo_26 is
		generic(
			N : natural := 119;
			N_SEM : natural := 36;
			N_MDC : natural := 14;
			N_CVS : natural := 33
		);
		port(
			Clock :  in std_logic;
			Reset :  in std_logic;
			Estado_i :  in std_logic;
			Estado_ante :  out std_logic;
			Estado_post :  out std_logic;
			Semaforo_propio_i_1 :  in sem_type;
			Semaforo_propio_o_1 :  out sem_type;
			Semaforo_cercano :  out sem_type;
			Estado_o :  out std_logic
		);
	end component nodo_26;
	component nodo_27 is
		generic(
			N : natural := 119;
			N_SEM : natural := 36;
			N_MDC : natural := 14;
			N_CVS : natural := 33
		);
		port(
			Clock :  in std_logic;
			Reset :  in std_logic;
			Estado_i :  in std_logic;
			Estado_post :  out std_logic;
			Semaforo_propio_i_1 :  in sem_type;
			Semaforo_propio_o_1 :  out sem_type;
			Semaforo_cercano :  out sem_type;
			Estado_o :  out std_logic
		);
	end component nodo_27;
	component nodo_28 is
		generic(
			N : natural := 119;
			N_SEM : natural := 36;
			N_MDC : natural := 14;
			N_CVS : natural := 33
		);
		port(
			Clock :  in std_logic;
			Reset :  in std_logic;
			Estado_i :  in std_logic;
			Estado_ante :  out std_logic;
			Estado_post :  out std_logic;
			Estado_o :  out std_logic
		);
	end component nodo_28;
	component nodo_29 is
		generic(
			N : natural := 119;
			N_SEM : natural := 36;
			N_MDC : natural := 14;
			N_CVS : natural := 33
		);
		port(
			Clock :  in std_logic;
			Reset :  in std_logic;
			Estado_i :  in std_logic;
			Estado_ante :  out std_logic;
			Estado_post :  out std_logic;
			Estado_o :  out std_logic
		);
	end component nodo_29;
	component nodo_30 is
		generic(
			N : natural := 119;
			N_SEM : natural := 36;
			N_MDC : natural := 14;
			N_CVS : natural := 33
		);
		port(
			Clock :  in std_logic;
			Reset :  in std_logic;
			Estado_i :  in std_logic;
			Estado_ante :  out std_logic;
			Estado_post :  out std_logic;
			Estado_o :  out std_logic
		);
	end component nodo_30;
	component nodo_31 is
		generic(
			N : natural := 119;
			N_SEM : natural := 36;
			N_MDC : natural := 14;
			N_CVS : natural := 33
		);
		port(
			Clock :  in std_logic;
			Reset :  in std_logic;
			Estado_i :  in std_logic;
			Estado_ante :  out std_logic;
			Estado_post :  out std_logic;
			Estado_o :  out std_logic
		);
	end component nodo_31;
	component nodo_32 is
		generic(
			N : natural := 119;
			N_SEM : natural := 36;
			N_MDC : natural := 14;
			N_CVS : natural := 33
		);
		port(
			Clock :  in std_logic;
			Reset :  in std_logic;
			Estado_i :  in std_logic;
			Estado_ante :  out std_logic;
			Estado_post :  out std_logic;
			Estado_o :  out std_logic
		);
	end component nodo_32;
	component nodo_33 is
		generic(
			N : natural := 119;
			N_SEM : natural := 36;
			N_MDC : natural := 14;
			N_CVS : natural := 33
		);
		port(
			Clock :  in std_logic;
			Reset :  in std_logic;
			Estado_i :  in std_logic;
			Estado_ante :  out std_logic;
			Semaforo_propio_i_1 :  in sem_type;
			Semaforo_propio_o_1 :  out sem_type;
			Semaforo_cercano :  out sem_type;
			Estado_o :  out std_logic
		);
	end component nodo_33;
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
	Signal conector_7 : std_logic;
	Signal ocupacion_7 : std_logic;
	Signal conector_8 : std_logic;
	Signal ocupacion_8 : std_logic;
	Signal conector_9 : std_logic;
	Signal ocupacion_9 : std_logic;
	Signal conector_10 : std_logic;
	Signal ocupacion_10 : std_logic;
	Signal conector_11 : std_logic;
	Signal ocupacion_11 : std_logic;
	Signal conector_12 : std_logic;
	Signal ocupacion_12 : std_logic;
	Signal conector_13 : std_logic;
	Signal ocupacion_13 : std_logic;
	Signal conector_14 : std_logic;
	Signal ocupacion_14 : std_logic;
	Signal conector_15 : std_logic;
	Signal ocupacion_15 : std_logic;
	Signal conector_16 : std_logic;
	Signal ocupacion_16 : std_logic;
	Signal conector_17 : std_logic;
	Signal ocupacion_17 : std_logic;
	Signal conector_18 : std_logic;
	Signal ocupacion_18 : std_logic;
	Signal conector_19 : std_logic;
	Signal ocupacion_19 : std_logic;
	Signal conector_20 : std_logic;
	Signal ocupacion_20 : std_logic;
	Signal conector_21 : std_logic;
	Signal ocupacion_21 : std_logic;
	Signal conector_22 : std_logic;
	Signal ocupacion_22 : std_logic;
	Signal conector_23 : std_logic;
	Signal ocupacion_23 : std_logic;
	Signal conector_24 : std_logic;
	Signal ocupacion_24 : std_logic;
	Signal conector_25 : std_logic;
	Signal ocupacion_25 : std_logic;
	Signal conector_26 : std_logic;
	Signal ocupacion_26 : std_logic;
	Signal conector_27 : std_logic;
	Signal ocupacion_27 : std_logic;
	Signal conector_28 : std_logic;
	Signal ocupacion_28 : std_logic;
	Signal conector_29 : std_logic;
	Signal ocupacion_29 : std_logic;
	Signal conector_30 : std_logic;
	Signal ocupacion_30 : std_logic;
	Signal conector_31 : std_logic;
	Signal ocupacion_31 : std_logic;
	Signal conector_32 : std_logic;
	Signal ocupacion_32 : std_logic;
	Signal conector_33 : std_logic;
	Signal ocupacion_33 : std_logic;
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
	Signal sem_lsb_i_8 : std_logic;
	Signal sem_msb_i_8 : std_logic;
	Signal sem_lsb_o_8 : std_logic;
	Signal sem_msb_o_8 : std_logic;
	Signal sem_lsb_i_9 : std_logic;
	Signal sem_msb_i_9 : std_logic;
	Signal sem_lsb_o_9 : std_logic;
	Signal sem_msb_o_9 : std_logic;
	Signal sem_lsb_i_10 : std_logic;
	Signal sem_msb_i_10 : std_logic;
	Signal sem_lsb_o_10 : std_logic;
	Signal sem_msb_o_10 : std_logic;
	Signal sem_lsb_i_11 : std_logic;
	Signal sem_msb_i_11 : std_logic;
	Signal sem_lsb_o_11 : std_logic;
	Signal sem_msb_o_11 : std_logic;
	Signal sem_lsb_i_12 : std_logic;
	Signal sem_msb_i_12 : std_logic;
	Signal sem_lsb_o_12 : std_logic;
	Signal sem_msb_o_12 : std_logic;
	Signal sem_lsb_i_13 : std_logic;
	Signal sem_msb_i_13 : std_logic;
	Signal sem_lsb_o_13 : std_logic;
	Signal sem_msb_o_13 : std_logic;
	Signal sem_lsb_i_14 : std_logic;
	Signal sem_msb_i_14 : std_logic;
	Signal sem_lsb_o_14 : std_logic;
	Signal sem_msb_o_14 : std_logic;
	Signal sem_lsb_i_15 : std_logic;
	Signal sem_msb_i_15 : std_logic;
	Signal sem_lsb_o_15 : std_logic;
	Signal sem_msb_o_15 : std_logic;
	Signal sem_lsb_i_16 : std_logic;
	Signal sem_msb_i_16 : std_logic;
	Signal sem_lsb_o_16 : std_logic;
	Signal sem_msb_o_16 : std_logic;
	Signal sem_lsb_i_17 : std_logic;
	Signal sem_msb_i_17 : std_logic;
	Signal sem_lsb_o_17 : std_logic;
	Signal sem_msb_o_17 : std_logic;
	Signal sem_lsb_i_18 : std_logic;
	Signal sem_msb_i_18 : std_logic;
	Signal sem_lsb_o_18 : std_logic;
	Signal sem_msb_o_18 : std_logic;
	Signal sem_lsb_i_19 : std_logic;
	Signal sem_msb_i_19 : std_logic;
	Signal sem_lsb_o_19 : std_logic;
	Signal sem_msb_o_19 : std_logic;
	Signal sem_lsb_i_20 : std_logic;
	Signal sem_msb_i_20 : std_logic;
	Signal sem_lsb_o_20 : std_logic;
	Signal sem_msb_o_20 : std_logic;
	Signal sem_lsb_i_21 : std_logic;
	Signal sem_msb_i_21 : std_logic;
	Signal sem_lsb_o_21 : std_logic;
	Signal sem_msb_o_21 : std_logic;
	Signal sem_lsb_i_22 : std_logic;
	Signal sem_msb_i_22 : std_logic;
	Signal sem_lsb_o_22 : std_logic;
	Signal sem_msb_o_22 : std_logic;
	Signal sem_lsb_i_23 : std_logic;
	Signal sem_msb_i_23 : std_logic;
	Signal sem_lsb_o_23 : std_logic;
	Signal sem_msb_o_23 : std_logic;
	Signal sem_lsb_i_24 : std_logic;
	Signal sem_msb_i_24 : std_logic;
	Signal sem_lsb_o_24 : std_logic;
	Signal sem_msb_o_24 : std_logic;
	Signal sem_lsb_i_25 : std_logic;
	Signal sem_msb_i_25 : std_logic;
	Signal sem_lsb_o_25 : std_logic;
	Signal sem_msb_o_25 : std_logic;
	Signal sem_lsb_i_26 : std_logic;
	Signal sem_msb_i_26 : std_logic;
	Signal sem_lsb_o_26 : std_logic;
	Signal sem_msb_o_26 : std_logic;
	Signal sem_lsb_i_27 : std_logic;
	Signal sem_msb_i_27 : std_logic;
	Signal sem_lsb_o_27 : std_logic;
	Signal sem_msb_o_27 : std_logic;
	Signal sem_lsb_i_28 : std_logic;
	Signal sem_msb_i_28 : std_logic;
	Signal sem_lsb_o_28 : std_logic;
	Signal sem_msb_o_28 : std_logic;
	Signal sem_lsb_i_29 : std_logic;
	Signal sem_msb_i_29 : std_logic;
	Signal sem_lsb_o_29 : std_logic;
	Signal sem_msb_o_29 : std_logic;
	Signal sem_lsb_i_30 : std_logic;
	Signal sem_msb_i_30 : std_logic;
	Signal sem_lsb_o_30 : std_logic;
	Signal sem_msb_o_30 : std_logic;
	Signal sem_lsb_i_31 : std_logic;
	Signal sem_msb_i_31 : std_logic;
	Signal sem_lsb_o_31 : std_logic;
	Signal sem_msb_o_31 : std_logic;
	Signal sem_lsb_i_32 : std_logic;
	Signal sem_msb_i_32 : std_logic;
	Signal sem_lsb_o_32 : std_logic;
	Signal sem_msb_o_32 : std_logic;
	Signal sem_lsb_i_33 : std_logic;
	Signal sem_msb_i_33 : std_logic;
	Signal sem_lsb_o_33 : std_logic;
	Signal sem_msb_o_33 : std_logic;
	Signal sem_lsb_i_34 : std_logic;
	Signal sem_msb_i_34 : std_logic;
	Signal sem_lsb_o_34 : std_logic;
	Signal sem_msb_o_34 : std_logic;
	Signal sem_lsb_i_35 : std_logic;
	Signal sem_msb_i_35 : std_logic;
	Signal sem_lsb_o_35 : std_logic;
	Signal sem_msb_o_35 : std_logic;
	Signal sem_lsb_i_36 : std_logic;
	Signal sem_msb_i_36 : std_logic;
	Signal sem_lsb_o_36 : std_logic;
	Signal sem_msb_o_36 : std_logic;
	Signal mdc_i_1 : std_logic;
	Signal mdc_o_1 : std_logic;
	Signal mdc_ante_i_1 : std_logic;
	Signal mdc_ante_o_1 : std_logic;
	Signal mdc_post_i_1 : std_logic;
	Signal mdc_post_o_1 : std_logic;
	Signal mdc_desv_i_1 : std_logic;
	Signal mdc_desv_o_1 : std_logic;
	Signal mdc_i_2 : std_logic;
	Signal mdc_o_2 : std_logic;
	Signal mdc_ante_i_2 : std_logic;
	Signal mdc_ante_o_2 : std_logic;
	Signal mdc_post_i_2 : std_logic;
	Signal mdc_post_o_2 : std_logic;
	Signal mdc_desv_i_2 : std_logic;
	Signal mdc_desv_o_2 : std_logic;
	Signal mdc_i_3 : std_logic;
	Signal mdc_o_3 : std_logic;
	Signal mdc_ante_i_3 : std_logic;
	Signal mdc_ante_o_3 : std_logic;
	Signal mdc_post_i_3 : std_logic;
	Signal mdc_post_o_3 : std_logic;
	Signal mdc_desv_i_3 : std_logic;
	Signal mdc_desv_o_3 : std_logic;
	Signal mdc_i_4 : std_logic;
	Signal mdc_o_4 : std_logic;
	Signal mdc_ante_i_4 : std_logic;
	Signal mdc_ante_o_4 : std_logic;
	Signal mdc_post_i_4 : std_logic;
	Signal mdc_post_o_4 : std_logic;
	Signal mdc_desv_i_4 : std_logic;
	Signal mdc_desv_o_4 : std_logic;
	Signal mdc_i_5 : std_logic;
	Signal mdc_o_5 : std_logic;
	Signal mdc_ante_i_5 : std_logic;
	Signal mdc_ante_o_5 : std_logic;
	Signal mdc_post_i_5 : std_logic;
	Signal mdc_post_o_5 : std_logic;
	Signal mdc_desv_i_5 : std_logic;
	Signal mdc_desv_o_5 : std_logic;
	Signal mdc_i_6 : std_logic;
	Signal mdc_o_6 : std_logic;
	Signal mdc_ante_i_6 : std_logic;
	Signal mdc_ante_o_6 : std_logic;
	Signal mdc_post_i_6 : std_logic;
	Signal mdc_post_o_6 : std_logic;
	Signal mdc_desv_i_6 : std_logic;
	Signal mdc_desv_o_6 : std_logic;
	Signal mdc_i_7 : std_logic;
	Signal mdc_o_7 : std_logic;
	Signal mdc_ante_i_7 : std_logic;
	Signal mdc_ante_o_7 : std_logic;
	Signal mdc_post_i_7 : std_logic;
	Signal mdc_post_o_7 : std_logic;
	Signal mdc_desv_i_7 : std_logic;
	Signal mdc_desv_o_7 : std_logic;
	Signal mdc_i_8 : std_logic;
	Signal mdc_o_8 : std_logic;
	Signal mdc_ante_i_8 : std_logic;
	Signal mdc_ante_o_8 : std_logic;
	Signal mdc_post_i_8 : std_logic;
	Signal mdc_post_o_8 : std_logic;
	Signal mdc_desv_i_8 : std_logic;
	Signal mdc_desv_o_8 : std_logic;
	Signal mdc_i_9 : std_logic;
	Signal mdc_o_9 : std_logic;
	Signal mdc_ante_i_9 : std_logic;
	Signal mdc_ante_o_9 : std_logic;
	Signal mdc_post_i_9 : std_logic;
	Signal mdc_post_o_9 : std_logic;
	Signal mdc_desv_i_9 : std_logic;
	Signal mdc_desv_o_9 : std_logic;
	Signal mdc_i_10 : std_logic;
	Signal mdc_o_10 : std_logic;
	Signal mdc_ante_i_10 : std_logic;
	Signal mdc_ante_o_10 : std_logic;
	Signal mdc_post_i_10 : std_logic;
	Signal mdc_post_o_10 : std_logic;
	Signal mdc_desv_i_10 : std_logic;
	Signal mdc_desv_o_10 : std_logic;
	Signal mdc_i_11 : std_logic;
	Signal mdc_o_11 : std_logic;
	Signal mdc_ante_i_11 : std_logic;
	Signal mdc_ante_o_11 : std_logic;
	Signal mdc_post_i_11 : std_logic;
	Signal mdc_post_o_11 : std_logic;
	Signal mdc_desv_i_11 : std_logic;
	Signal mdc_desv_o_11 : std_logic;
	Signal mdc_i_12 : std_logic;
	Signal mdc_o_12 : std_logic;
	Signal mdc_ante_i_12 : std_logic;
	Signal mdc_ante_o_12 : std_logic;
	Signal mdc_post_i_12 : std_logic;
	Signal mdc_post_o_12 : std_logic;
	Signal mdc_desv_i_12 : std_logic;
	Signal mdc_desv_o_12 : std_logic;
	Signal mdc_i_13 : std_logic;
	Signal mdc_o_13 : std_logic;
	Signal mdc_ante_i_13 : std_logic;
	Signal mdc_ante_o_13 : std_logic;
	Signal mdc_post_i_13 : std_logic;
	Signal mdc_post_o_13 : std_logic;
	Signal mdc_desv_i_13 : std_logic;
	Signal mdc_desv_o_13 : std_logic;
	Signal mdc_i_14 : std_logic;
	Signal mdc_o_14 : std_logic;
	Signal mdc_ante_i_14 : std_logic;
	Signal mdc_ante_o_14 : std_logic;
	Signal mdc_post_i_14 : std_logic;
	Signal mdc_post_o_14 : std_logic;
	Signal mdc_desv_i_14 : std_logic;
	Signal mdc_desv_o_14 : std_logic;
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
		Estado_i => ocupacion_2,
		Estado_o => conector_2,
		Reset => Reset
		);
	nodo_3_i:nodo_3 port map(
		Clock => Clock,
		Estado_ante => mdc_post_o_2,
		Estado_post => conector_4,
		Semaforo_propio_i_1.lsb => sem_lsb_i_4,
		Semaforo_propio_i_1.msb => sem_msb_i_4,
		Semaforo_propio_o_1.lsb => sem_lsb_o_4,
		Semaforo_propio_o_1.msb => sem_msb_o_4,
		Estado_i => ocupacion_3,
		Estado_o => conector_3,
		Reset => Reset
		);
	nodo_4_i:nodo_4 port map(
		Clock => Clock,
		Estado_ante => conector_3,
		Estado_post => mdc_ante_o_3,
		Semaforo_propio_i_1.lsb => sem_lsb_i_5,
		Semaforo_propio_i_1.msb => sem_msb_i_5,
		Semaforo_propio_o_1.lsb => sem_lsb_o_5,
		Semaforo_propio_o_1.msb => sem_msb_o_5,
		Semaforo_propio_i_2.lsb => sem_lsb_i_6,
		Semaforo_propio_i_2.msb => sem_msb_i_6,
		Semaforo_propio_o_2.lsb => sem_lsb_o_6,
		Semaforo_propio_o_2.msb => sem_msb_o_6,
		Semaforo_propio_i_3.lsb => sem_lsb_i_7,
		Semaforo_propio_i_3.msb => sem_msb_i_7,
		Semaforo_propio_o_3.lsb => sem_lsb_o_7,
		Semaforo_propio_o_3.msb => sem_msb_o_7,
		Semaforo_cercano.lsb => cosa,
		Semaforo_cercano.msb => cosa,
		Estado_i => ocupacion_4,
		Estado_o => conector_4,
		Reset => Reset
		);
	nodo_5_i:nodo_5 port map(
		Clock => Clock,
		Estado_ante => mdc_post_o_3,
		Estado_post => conector_7,
		Estado_i => ocupacion_5,
		Estado_o => conector_5,
		Reset => Reset
		);
	nodo_6_i:nodo_6 port map(
		Clock => Clock,
		Estado_post => mdc_desv_o_3,
		Estado_ante => mdc_desv_o_3,
		Estado_post => mdc_ante_o_4,
		Semaforo_propio_i_1.lsb => sem_lsb_i_8,
		Semaforo_propio_i_1.msb => sem_msb_i_8,
		Semaforo_propio_o_1.lsb => sem_lsb_o_8,
		Semaforo_propio_o_1.msb => sem_msb_o_8,
		Semaforo_propio_i_2.lsb => sem_lsb_i_9,
		Semaforo_propio_i_2.msb => sem_msb_i_9,
		Semaforo_propio_o_2.lsb => sem_lsb_o_9,
		Semaforo_propio_o_2.msb => sem_msb_o_9,
		Semaforo_cercano.lsb => cosa,
		Semaforo_cercano.msb => cosa,
		Estado_i => ocupacion_6,
		Estado_o => conector_6,
		Reset => Reset
		);
	nodo_7_i:nodo_7 port map(
		Clock => Clock,
		Estado_ante => conector_5,
		Estado_post => mdc_ante_o_6,
		Estado_i => ocupacion_7,
		Estado_o => conector_7,
		Reset => Reset
		);
	nodo_8_i:nodo_8 port map(
		Clock => Clock,
		Estado_ante => mdc_post_o_4,
		Estado_post => conector_11,
		Estado_i => ocupacion_8,
		Estado_o => conector_8,
		Reset => Reset
		);
	nodo_9_i:nodo_9 port map(
		Clock => Clock,
		Estado_post => conector_12,
		Estado_ante => mdc_post_o_5,
		Semaforo_propio_i_1.lsb => sem_lsb_i_10,
		Semaforo_propio_i_1.msb => sem_msb_i_10,
		Semaforo_propio_o_1.lsb => sem_lsb_o_10,
		Semaforo_propio_o_1.msb => sem_msb_o_10,
		Semaforo_propio_i_2.lsb => sem_lsb_i_11,
		Semaforo_propio_i_2.msb => sem_msb_i_11,
		Semaforo_propio_o_2.lsb => sem_lsb_o_11,
		Semaforo_propio_o_2.msb => sem_msb_o_11,
		Semaforo_propio_i_3.lsb => sem_lsb_i_12,
		Semaforo_propio_i_3.msb => sem_msb_i_12,
		Semaforo_propio_o_3.lsb => sem_lsb_o_12,
		Semaforo_propio_o_3.msb => sem_msb_o_12,
		Estado_i => ocupacion_9,
		Estado_o => conector_9,
		Reset => Reset
		);
	nodo_10_i:nodo_10 port map(
		Clock => Clock,
		Estado_ante => mdc_post_o_6,
		Estado_post => conector_13,
		Semaforo_propio_i_1.lsb => sem_lsb_i_13,
		Semaforo_propio_i_1.msb => sem_msb_i_13,
		Semaforo_propio_o_1.lsb => sem_lsb_o_13,
		Semaforo_propio_o_1.msb => sem_msb_o_13,
		Semaforo_propio_i_2.lsb => sem_lsb_i_14,
		Semaforo_propio_i_2.msb => sem_msb_i_14,
		Semaforo_propio_o_2.lsb => sem_lsb_o_14,
		Semaforo_propio_o_2.msb => sem_msb_o_14,
		Semaforo_propio_i_3.lsb => sem_lsb_i_15,
		Semaforo_propio_i_3.msb => sem_msb_i_15,
		Semaforo_propio_o_3.lsb => sem_lsb_o_15,
		Semaforo_propio_o_3.msb => sem_msb_o_15,
		Semaforo_cercano.lsb => cosa,
		Semaforo_cercano.msb => cosa,
		Estado_i => ocupacion_10,
		Estado_o => conector_10,
		Reset => Reset
		);
	nodo_11_i:nodo_11 port map(
		Clock => Clock,
		Estado_ante => conector_8,
		Estado_post => mdc_ante_o_8,
		Estado_i => ocupacion_11,
		Estado_o => conector_11,
		Reset => Reset
		);
	nodo_12_i:nodo_12 port map(
		Clock => Clock,
		Estado_ante => conector_9,
		Estado_post => mdc_ante_o_7,
		Semaforo_propio_i_1.lsb => sem_lsb_i_16,
		Semaforo_propio_i_1.msb => sem_msb_i_16,
		Semaforo_propio_o_1.lsb => sem_lsb_o_16,
		Semaforo_propio_o_1.msb => sem_msb_o_16,
		Semaforo_propio_i_2.lsb => sem_lsb_i_17,
		Semaforo_propio_i_2.msb => sem_msb_i_17,
		Semaforo_propio_o_2.lsb => sem_lsb_o_17,
		Semaforo_propio_o_2.msb => sem_msb_o_17,
		Estado_i => ocupacion_12,
		Estado_o => conector_12,
		Reset => Reset
		);
	nodo_13_i:nodo_13 port map(
		Clock => Clock,
		Estado_ante => conector_10,
		Estado_post => conector_15,
		Estado_i => ocupacion_13,
		Estado_o => conector_13,
		Reset => Reset
		);
	nodo_14_i:nodo_14 port map(
		Clock => Clock,
		Estado_ante => mdc_post_o_8,
		Estado_post => conector_16,
		Semaforo_propio_i_1.lsb => sem_lsb_i_18,
		Semaforo_propio_i_1.msb => sem_msb_i_18,
		Semaforo_propio_o_1.lsb => sem_lsb_o_18,
		Semaforo_propio_o_1.msb => sem_msb_o_18,
		Semaforo_propio_i_2.lsb => sem_lsb_i_19,
		Semaforo_propio_i_2.msb => sem_msb_i_19,
		Semaforo_propio_o_2.lsb => sem_lsb_o_19,
		Semaforo_propio_o_2.msb => sem_msb_o_19,
		Semaforo_cercano.lsb => cosa,
		Semaforo_cercano.msb => cosa,
		Estado_i => ocupacion_14,
		Estado_o => conector_14,
		Reset => Reset
		);
	nodo_15_i:nodo_15 port map(
		Clock => Clock,
		Estado_ante => conector_13,
		Estado_post => mdc_ante_o_9,
		Semaforo_propio_i_1.lsb => sem_lsb_i_20,
		Semaforo_propio_i_1.msb => sem_msb_i_20,
		Semaforo_propio_o_1.lsb => sem_lsb_o_20,
		Semaforo_propio_o_1.msb => sem_msb_o_20,
		Semaforo_propio_i_2.lsb => sem_lsb_i_21,
		Semaforo_propio_i_2.msb => sem_msb_i_21,
		Semaforo_propio_o_2.lsb => sem_lsb_o_21,
		Semaforo_propio_o_2.msb => sem_msb_o_21,
		Semaforo_cercano.lsb => cosa,
		Semaforo_cercano.msb => cosa,
		Estado_i => ocupacion_15,
		Estado_o => conector_15,
		Reset => Reset
		);
	nodo_16_i:nodo_16 port map(
		Clock => Clock,
		Estado_ante => conector_14,
		Estado_post => mdc_ante_o_10,
		Semaforo_propio_i_1.lsb => sem_lsb_i_22,
		Semaforo_propio_i_1.msb => sem_msb_i_22,
		Semaforo_propio_o_1.lsb => sem_lsb_o_22,
		Semaforo_propio_o_1.msb => sem_msb_o_22,
		Estado_i => ocupacion_16,
		Estado_o => conector_16,
		Reset => Reset
		);
	nodo_17_i:nodo_17 port map(
		Clock => Clock,
		Estado_ante => mdc_post_o_11,
		Estado_post => conector_19,
		Semaforo_propio_i_1.lsb => sem_lsb_i_23,
		Semaforo_propio_i_1.msb => sem_msb_i_23,
		Semaforo_propio_o_1.lsb => sem_lsb_o_23,
		Semaforo_propio_o_1.msb => sem_msb_o_23,
		Semaforo_propio_i_2.lsb => sem_lsb_i_24,
		Semaforo_propio_i_2.msb => sem_msb_i_24,
		Semaforo_propio_o_2.lsb => sem_lsb_o_24,
		Semaforo_propio_o_2.msb => sem_msb_o_24,
		Estado_i => ocupacion_17,
		Estado_o => conector_17,
		Reset => Reset
		);
	nodo_18_i:nodo_18 port map(
		Clock => Clock,
		Estado_ante => mdc_post_o_12,
		Estado_post => conector_20,
		Semaforo_propio_i_1.lsb => sem_lsb_i_25,
		Semaforo_propio_i_1.msb => sem_msb_i_25,
		Semaforo_propio_o_1.lsb => sem_lsb_o_25,
		Semaforo_propio_o_1.msb => sem_msb_o_25,
		Semaforo_propio_i_2.lsb => sem_lsb_i_26,
		Semaforo_propio_i_2.msb => sem_msb_i_26,
		Semaforo_propio_o_2.lsb => sem_lsb_o_26,
		Semaforo_propio_o_2.msb => sem_msb_o_26,
		Estado_i => ocupacion_18,
		Estado_o => conector_18,
		Reset => Reset
		);
	nodo_19_i:nodo_19 port map(
		Clock => Clock,
		Estado_ante => conector_17,
		Semaforo_propio_i_1.lsb => sem_lsb_i_27,
		Semaforo_propio_i_1.msb => sem_msb_i_27,
		Semaforo_propio_o_1.lsb => sem_lsb_o_27,
		Semaforo_propio_o_1.msb => sem_msb_o_27,
		Semaforo_cercano.lsb => cosa,
		Semaforo_cercano.msb => cosa,
		Estado_i => ocupacion_19,
		Estado_o => conector_19,
		Reset => Reset
		);
	nodo_20_i:nodo_20 port map(
		Clock => Clock,
		Estado_ante => conector_18,
		Semaforo_propio_i_1.lsb => sem_lsb_i_28,
		Semaforo_propio_i_1.msb => sem_msb_i_28,
		Semaforo_propio_o_1.lsb => sem_lsb_o_28,
		Semaforo_propio_o_1.msb => sem_msb_o_28,
		Semaforo_cercano.lsb => cosa,
		Semaforo_cercano.msb => cosa,
		Estado_i => ocupacion_20,
		Estado_o => conector_20,
		Reset => Reset
		);
	nodo_21_i:nodo_21 port map(
		Clock => Clock,
		Estado_post => conector_22,
		Semaforo_propio_i_1.lsb => sem_lsb_i_29,
		Semaforo_propio_i_1.msb => sem_msb_i_29,
		Semaforo_propio_o_1.lsb => sem_lsb_o_29,
		Semaforo_propio_o_1.msb => sem_msb_o_29,
		Semaforo_cercano.lsb => cosa,
		Semaforo_cercano.msb => cosa,
		Estado_i => ocupacion_21,
		Estado_o => conector_21,
		Reset => Reset
		);
	nodo_22_i:nodo_22 port map(
		Clock => Clock,
		Estado_ante => conector_21,
		Estado_post => mdc_ante_o_13,
		Semaforo_propio_i_1.lsb => sem_lsb_i_30,
		Semaforo_propio_i_1.msb => sem_msb_i_30,
		Semaforo_propio_o_1.lsb => sem_lsb_o_30,
		Semaforo_propio_o_1.msb => sem_msb_o_30,
		Semaforo_propio_i_2.lsb => sem_lsb_i_31,
		Semaforo_propio_i_2.msb => sem_msb_i_31,
		Semaforo_propio_o_2.lsb => sem_lsb_o_31,
		Semaforo_propio_o_2.msb => sem_msb_o_31,
		Estado_i => ocupacion_22,
		Estado_o => conector_22,
		Reset => Reset
		);
	nodo_23_i:nodo_23 port map(
		Clock => Clock,
		Estado_ante => mdc_post_o_14,
		Estado_post => conector_24,
		Semaforo_propio_i_1.lsb => sem_lsb_i_32,
		Semaforo_propio_i_1.msb => sem_msb_i_32,
		Semaforo_propio_o_1.lsb => sem_lsb_o_32,
		Semaforo_propio_o_1.msb => sem_msb_o_32,
		Semaforo_propio_i_2.lsb => sem_lsb_i_33,
		Semaforo_propio_i_2.msb => sem_msb_i_33,
		Semaforo_propio_o_2.lsb => sem_lsb_o_33,
		Semaforo_propio_o_2.msb => sem_msb_o_33,
		Semaforo_cercano.lsb => cosa,
		Semaforo_cercano.msb => cosa,
		Estado_i => ocupacion_23,
		Estado_o => conector_23,
		Reset => Reset
		);
	nodo_24_i:nodo_24 port map(
		Clock => Clock,
		Estado_ante => conector_23,
		Estado_post => conector_25,
		Estado_i => ocupacion_24,
		Estado_o => conector_24,
		Reset => Reset
		);
	nodo_25_i:nodo_25 port map(
		Clock => Clock,
		Estado_ante => conector_24,
		Estado_post => conector_26,
		Estado_i => ocupacion_25,
		Estado_o => conector_25,
		Reset => Reset
		);
	nodo_26_i:nodo_26 port map(
		Clock => Clock,
		Estado_ante => conector_25,
		Estado_post => mdc_desv_o_6,
		Semaforo_propio_i_1.lsb => sem_lsb_i_34,
		Semaforo_propio_i_1.msb => sem_msb_i_34,
		Semaforo_propio_o_1.lsb => sem_lsb_o_34,
		Semaforo_propio_o_1.msb => sem_msb_o_34,
		Semaforo_cercano.lsb => cosa,
		Semaforo_cercano.msb => cosa,
		Estado_i => ocupacion_26,
		Estado_o => conector_26,
		Reset => Reset
		);
	nodo_27_i:nodo_27 port map(
		Clock => Clock,
		Estado_post => conector_28,
		Semaforo_propio_i_1.lsb => sem_lsb_i_35,
		Semaforo_propio_i_1.msb => sem_msb_i_35,
		Semaforo_propio_o_1.lsb => sem_lsb_o_35,
		Semaforo_propio_o_1.msb => sem_msb_o_35,
		Semaforo_cercano.lsb => cosa,
		Semaforo_cercano.msb => cosa,
		Estado_i => ocupacion_27,
		Estado_o => conector_27,
		Reset => Reset
		);
	nodo_28_i:nodo_28 port map(
		Clock => Clock,
		Estado_ante => conector_27,
		Estado_post => conector_29,
		Estado_i => ocupacion_28,
		Estado_o => conector_28,
		Reset => Reset
		);
	nodo_29_i:nodo_29 port map(
		Clock => Clock,
		Estado_ante => conector_28,
		Estado_post => mdc_ante_o_5,
		Estado_i => ocupacion_29,
		Estado_o => conector_29,
		Reset => Reset
		);
	nodo_30_i:nodo_30 port map(
		Clock => Clock,
		Estado_ante => mdc_post_o_7,
		Estado_post => conector_31,
		Estado_i => ocupacion_30,
		Estado_o => conector_30,
		Reset => Reset
		);
	nodo_31_i:nodo_31 port map(
		Clock => Clock,
		Estado_ante => conector_30,
		Estado_post => conector_32,
		Estado_i => ocupacion_31,
		Estado_o => conector_31,
		Reset => Reset
		);
	nodo_32_i:nodo_32 port map(
		Clock => Clock,
		Estado_ante => conector_31,
		Estado_post => conector_33,
		Estado_i => ocupacion_32,
		Estado_o => conector_32,
		Reset => Reset
		);
	nodo_33_i:nodo_33 port map(
		Clock => Clock,
		Estado_ante => conector_32,
		Semaforo_propio_i_1.lsb => sem_lsb_i_36,
		Semaforo_propio_i_1.msb => sem_msb_i_36,
		Semaforo_propio_o_1.lsb => sem_lsb_o_36,
		Semaforo_propio_o_1.msb => sem_msb_o_36,
		Semaforo_cercano.lsb => cosa,
		Semaforo_cercano.msb => cosa,
		Estado_i => ocupacion_33,
		Estado_o => conector_33,
		Reset => Reset
		);
	cambio_1_i:cambio_1 port map(
		Clock => Clock,
		Cambio_i => mdc_i_1,
		Cambio_o => mdc_o_1,
		Estado_ante_i => conector_2,
		Estado_ante_o => mdc_ante_o_1,
		Estado_post_i => conector_0,
		Estado_post_o => mdc_post_o_1,
		Estado_desv_i => conector_0,
		Estado_desv_o => mdc_desv_o_1,
		Reset => Reset
		);
	cambio_2_i:cambio_2 port map(
		Clock => Clock,
		Cambio_i => mdc_i_2,
		Cambio_o => mdc_o_2,
		Estado_ante_i => conector_0,
		Estado_ante_o => mdc_ante_o_2,
		Estado_post_i => conector_0,
		Estado_post_o => mdc_post_o_2,
		Estado_desv_i => conector_0,
		Estado_desv_o => mdc_desv_o_2,
		Reset => Reset
		);
	cambio_3_i:cambio_3 port map(
		Clock => Clock,
		Cambio_i => mdc_i_3,
		Cambio_o => mdc_o_3,
		Estado_ante_i => conector_4,
		Estado_ante_o => mdc_ante_o_3,
		Estado_post_i => conector_5,
		Estado_post_o => mdc_post_o_3,
		Estado_desv_i => conector_6,
		Estado_desv_o => mdc_desv_o_3,
		Reset => Reset
		);
	cambio_4_i:cambio_4 port map(
		Clock => Clock,
		Cambio_i => mdc_i_4,
		Cambio_o => mdc_o_4,
		Estado_ante_i => conector_6,
		Estado_ante_o => mdc_ante_o_4,
		Estado_post_i => conector_8,
		Estado_post_o => mdc_post_o_4,
		Estado_desv_i => conector_0,
		Estado_desv_o => mdc_desv_o_4,
		Reset => Reset
		);
	cambio_5_i:cambio_5 port map(
		Clock => Clock,
		Cambio_i => mdc_i_5,
		Cambio_o => mdc_o_5,
		Estado_ante_i => conector_0,
		Estado_ante_o => mdc_ante_o_5,
		Estado_post_i => conector_29,
		Estado_post_o => mdc_post_o_5,
		Estado_desv_i => conector_0,
		Estado_desv_o => mdc_desv_o_5,
		Reset => Reset
		);
	cambio_6_i:cambio_6 port map(
		Clock => Clock,
		Cambio_i => mdc_i_6,
		Cambio_o => mdc_o_6,
		Estado_ante_i => conector_0,
		Estado_ante_o => mdc_ante_o_6,
		Estado_post_i => conector_7,
		Estado_post_o => mdc_post_o_6,
		Estado_desv_i => conector_26,
		Estado_desv_o => mdc_desv_o_6,
		Reset => Reset
		);
	cambio_7_i:cambio_7 port map(
		Clock => Clock,
		Cambio_i => mdc_i_7,
		Cambio_o => mdc_o_7,
		Estado_ante_i => conector_12,
		Estado_ante_o => mdc_ante_o_7,
		Estado_post_i => conector_30,
		Estado_post_o => mdc_post_o_7,
		Estado_desv_i => conector_0,
		Estado_desv_o => mdc_desv_o_7,
		Reset => Reset
		);
	cambio_8_i:cambio_8 port map(
		Clock => Clock,
		Cambio_i => mdc_i_8,
		Cambio_o => mdc_o_8,
		Estado_ante_i => conector_0,
		Estado_ante_o => mdc_ante_o_8,
		Estado_post_i => conector_11,
		Estado_post_o => mdc_post_o_8,
		Estado_desv_i => conector_0,
		Estado_desv_o => mdc_desv_o_8,
		Reset => Reset
		);
	cambio_9_i:cambio_9 port map(
		Clock => Clock,
		Cambio_i => mdc_i_9,
		Cambio_o => mdc_o_9,
		Estado_ante_i => conector_15,
		Estado_ante_o => mdc_ante_o_9,
		Estado_post_i => conector_0,
		Estado_post_o => mdc_post_o_9,
		Estado_desv_i => conector_0,
		Estado_desv_o => mdc_desv_o_9,
		Reset => Reset
		);
	cambio_10_i:cambio_10 port map(
		Clock => Clock,
		Cambio_i => mdc_i_10,
		Cambio_o => mdc_o_10,
		Estado_ante_i => conector_16,
		Estado_ante_o => mdc_ante_o_10,
		Estado_post_i => conector_0,
		Estado_post_o => mdc_post_o_10,
		Estado_desv_i => conector_0,
		Estado_desv_o => mdc_desv_o_10,
		Reset => Reset
		);
	cambio_11_i:cambio_11 port map(
		Clock => Clock,
		Cambio_i => mdc_i_11,
		Cambio_o => mdc_o_11,
		Estado_ante_i => conector_0,
		Estado_ante_o => mdc_ante_o_11,
		Estado_post_i => conector_0,
		Estado_post_o => mdc_post_o_11,
		Estado_desv_i => conector_0,
		Estado_desv_o => mdc_desv_o_11,
		Reset => Reset
		);
	cambio_12_i:cambio_12 port map(
		Clock => Clock,
		Cambio_i => mdc_i_12,
		Cambio_o => mdc_o_12,
		Estado_ante_i => conector_0,
		Estado_ante_o => mdc_ante_o_12,
		Estado_post_i => conector_0,
		Estado_post_o => mdc_post_o_12,
		Estado_desv_i => conector_0,
		Estado_desv_o => mdc_desv_o_12,
		Reset => Reset
		);
	cambio_13_i:cambio_13 port map(
		Clock => Clock,
		Cambio_i => mdc_i_13,
		Cambio_o => mdc_o_13,
		Estado_ante_i => conector_22,
		Estado_ante_o => mdc_ante_o_13,
		Estado_post_i => conector_0,
		Estado_post_o => mdc_post_o_13,
		Estado_desv_i => conector_0,
		Estado_desv_o => mdc_desv_o_13,
		Reset => Reset
		);
	cambio_14_i:cambio_14 port map(
		Clock => Clock,
		Cambio_i => mdc_i_14,
		Cambio_o => mdc_o_14,
		Estado_ante_i => conector_0,
		Estado_ante_o => mdc_ante_o_14,
		Estado_post_i => conector_0,
		Estado_post_o => mdc_post_o_14,
		Estado_desv_i => conector_0,
		Estado_desv_o => mdc_desv_o_14,
		Reset => Reset
		);
		cosa <= '0';
		ocupacion_1 <= Ocupacion(0);
		ocupacion_2 <= Ocupacion(1);
		ocupacion_3 <= Ocupacion(2);
		ocupacion_4 <= Ocupacion(3);
		ocupacion_5 <= Ocupacion(4);
		ocupacion_6 <= Ocupacion(5);
		ocupacion_7 <= Ocupacion(6);
		ocupacion_8 <= Ocupacion(7);
		ocupacion_9 <= Ocupacion(8);
		ocupacion_10 <= Ocupacion(9);
		ocupacion_11 <= Ocupacion(10);
		ocupacion_12 <= Ocupacion(11);
		ocupacion_13 <= Ocupacion(12);
		ocupacion_14 <= Ocupacion(13);
		ocupacion_15 <= Ocupacion(14);
		ocupacion_16 <= Ocupacion(15);
		ocupacion_17 <= Ocupacion(16);
		ocupacion_18 <= Ocupacion(17);
		ocupacion_19 <= Ocupacion(18);
		ocupacion_20 <= Ocupacion(19);
		ocupacion_21 <= Ocupacion(20);
		ocupacion_22 <= Ocupacion(21);
		ocupacion_23 <= Ocupacion(22);
		ocupacion_24 <= Ocupacion(23);
		ocupacion_25 <= Ocupacion(24);
		ocupacion_26 <= Ocupacion(25);
		ocupacion_27 <= Ocupacion(26);
		ocupacion_28 <= Ocupacion(27);
		ocupacion_29 <= Ocupacion(28);
		ocupacion_30 <= Ocupacion(29);
		ocupacion_31 <= Ocupacion(30);
		ocupacion_32 <= Ocupacion(31);
		ocupacion_33 <= Ocupacion(32);
		mdc_i_1 <= Cambios_i(0);
		Cambios_o(0) <= mdc_o_1;
		mdc_i_2 <= Cambios_i(1);
		Cambios_o(1) <= mdc_o_2;
		mdc_i_3 <= Cambios_i(2);
		Cambios_o(2) <= mdc_o_3;
		mdc_i_4 <= Cambios_i(3);
		Cambios_o(3) <= mdc_o_4;
		mdc_i_5 <= Cambios_i(4);
		Cambios_o(4) <= mdc_o_5;
		mdc_i_6 <= Cambios_i(5);
		Cambios_o(5) <= mdc_o_6;
		mdc_i_7 <= Cambios_i(6);
		Cambios_o(6) <= mdc_o_7;
		mdc_i_8 <= Cambios_i(7);
		Cambios_o(7) <= mdc_o_8;
		mdc_i_9 <= Cambios_i(8);
		Cambios_o(8) <= mdc_o_9;
		mdc_i_10 <= Cambios_i(9);
		Cambios_o(9) <= mdc_o_10;
		mdc_i_11 <= Cambios_i(10);
		Cambios_o(10) <= mdc_o_11;
		mdc_i_12 <= Cambios_i(11);
		Cambios_o(11) <= mdc_o_12;
		mdc_i_13 <= Cambios_i(12);
		Cambios_o(12) <= mdc_o_13;
		mdc_i_14 <= Cambios_i(13);
		Cambios_o(13) <= mdc_o_14;
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
		sem_lsb_i_8 <= semaforos_i.lsb(7);
		sem_msb_i_8 <= semaforos_i.msb(7);
		semaforos_o.lsb(7) <= sem_lsb_o_8;
		semaforos_o.msb(7) <= sem_msb_o_8;
		sem_lsb_i_9 <= semaforos_i.lsb(8);
		sem_msb_i_9 <= semaforos_i.msb(8);
		semaforos_o.lsb(8) <= sem_lsb_o_9;
		semaforos_o.msb(8) <= sem_msb_o_9;
		sem_lsb_i_10 <= semaforos_i.lsb(9);
		sem_msb_i_10 <= semaforos_i.msb(9);
		semaforos_o.lsb(9) <= sem_lsb_o_10;
		semaforos_o.msb(9) <= sem_msb_o_10;
		sem_lsb_i_11 <= semaforos_i.lsb(10);
		sem_msb_i_11 <= semaforos_i.msb(10);
		semaforos_o.lsb(10) <= sem_lsb_o_11;
		semaforos_o.msb(10) <= sem_msb_o_11;
		sem_lsb_i_12 <= semaforos_i.lsb(11);
		sem_msb_i_12 <= semaforos_i.msb(11);
		semaforos_o.lsb(11) <= sem_lsb_o_12;
		semaforos_o.msb(11) <= sem_msb_o_12;
		sem_lsb_i_13 <= semaforos_i.lsb(12);
		sem_msb_i_13 <= semaforos_i.msb(12);
		semaforos_o.lsb(12) <= sem_lsb_o_13;
		semaforos_o.msb(12) <= sem_msb_o_13;
		sem_lsb_i_14 <= semaforos_i.lsb(13);
		sem_msb_i_14 <= semaforos_i.msb(13);
		semaforos_o.lsb(13) <= sem_lsb_o_14;
		semaforos_o.msb(13) <= sem_msb_o_14;
		sem_lsb_i_15 <= semaforos_i.lsb(14);
		sem_msb_i_15 <= semaforos_i.msb(14);
		semaforos_o.lsb(14) <= sem_lsb_o_15;
		semaforos_o.msb(14) <= sem_msb_o_15;
		sem_lsb_i_16 <= semaforos_i.lsb(15);
		sem_msb_i_16 <= semaforos_i.msb(15);
		semaforos_o.lsb(15) <= sem_lsb_o_16;
		semaforos_o.msb(15) <= sem_msb_o_16;
		sem_lsb_i_17 <= semaforos_i.lsb(16);
		sem_msb_i_17 <= semaforos_i.msb(16);
		semaforos_o.lsb(16) <= sem_lsb_o_17;
		semaforos_o.msb(16) <= sem_msb_o_17;
		sem_lsb_i_18 <= semaforos_i.lsb(17);
		sem_msb_i_18 <= semaforos_i.msb(17);
		semaforos_o.lsb(17) <= sem_lsb_o_18;
		semaforos_o.msb(17) <= sem_msb_o_18;
		sem_lsb_i_19 <= semaforos_i.lsb(18);
		sem_msb_i_19 <= semaforos_i.msb(18);
		semaforos_o.lsb(18) <= sem_lsb_o_19;
		semaforos_o.msb(18) <= sem_msb_o_19;
		sem_lsb_i_20 <= semaforos_i.lsb(19);
		sem_msb_i_20 <= semaforos_i.msb(19);
		semaforos_o.lsb(19) <= sem_lsb_o_20;
		semaforos_o.msb(19) <= sem_msb_o_20;
		sem_lsb_i_21 <= semaforos_i.lsb(20);
		sem_msb_i_21 <= semaforos_i.msb(20);
		semaforos_o.lsb(20) <= sem_lsb_o_21;
		semaforos_o.msb(20) <= sem_msb_o_21;
		sem_lsb_i_22 <= semaforos_i.lsb(21);
		sem_msb_i_22 <= semaforos_i.msb(21);
		semaforos_o.lsb(21) <= sem_lsb_o_22;
		semaforos_o.msb(21) <= sem_msb_o_22;
		sem_lsb_i_23 <= semaforos_i.lsb(22);
		sem_msb_i_23 <= semaforos_i.msb(22);
		semaforos_o.lsb(22) <= sem_lsb_o_23;
		semaforos_o.msb(22) <= sem_msb_o_23;
		sem_lsb_i_24 <= semaforos_i.lsb(23);
		sem_msb_i_24 <= semaforos_i.msb(23);
		semaforos_o.lsb(23) <= sem_lsb_o_24;
		semaforos_o.msb(23) <= sem_msb_o_24;
		sem_lsb_i_25 <= semaforos_i.lsb(24);
		sem_msb_i_25 <= semaforos_i.msb(24);
		semaforos_o.lsb(24) <= sem_lsb_o_25;
		semaforos_o.msb(24) <= sem_msb_o_25;
		sem_lsb_i_26 <= semaforos_i.lsb(25);
		sem_msb_i_26 <= semaforos_i.msb(25);
		semaforos_o.lsb(25) <= sem_lsb_o_26;
		semaforos_o.msb(25) <= sem_msb_o_26;
		sem_lsb_i_27 <= semaforos_i.lsb(26);
		sem_msb_i_27 <= semaforos_i.msb(26);
		semaforos_o.lsb(26) <= sem_lsb_o_27;
		semaforos_o.msb(26) <= sem_msb_o_27;
		sem_lsb_i_28 <= semaforos_i.lsb(27);
		sem_msb_i_28 <= semaforos_i.msb(27);
		semaforos_o.lsb(27) <= sem_lsb_o_28;
		semaforos_o.msb(27) <= sem_msb_o_28;
		sem_lsb_i_29 <= semaforos_i.lsb(28);
		sem_msb_i_29 <= semaforos_i.msb(28);
		semaforos_o.lsb(28) <= sem_lsb_o_29;
		semaforos_o.msb(28) <= sem_msb_o_29;
		sem_lsb_i_30 <= semaforos_i.lsb(29);
		sem_msb_i_30 <= semaforos_i.msb(29);
		semaforos_o.lsb(29) <= sem_lsb_o_30;
		semaforos_o.msb(29) <= sem_msb_o_30;
		sem_lsb_i_31 <= semaforos_i.lsb(30);
		sem_msb_i_31 <= semaforos_i.msb(30);
		semaforos_o.lsb(30) <= sem_lsb_o_31;
		semaforos_o.msb(30) <= sem_msb_o_31;
		sem_lsb_i_32 <= semaforos_i.lsb(31);
		sem_msb_i_32 <= semaforos_i.msb(31);
		semaforos_o.lsb(31) <= sem_lsb_o_32;
		semaforos_o.msb(31) <= sem_msb_o_32;
		sem_lsb_i_33 <= semaforos_i.lsb(32);
		sem_msb_i_33 <= semaforos_i.msb(32);
		semaforos_o.lsb(32) <= sem_lsb_o_33;
		semaforos_o.msb(32) <= sem_msb_o_33;
		sem_lsb_i_34 <= semaforos_i.lsb(33);
		sem_msb_i_34 <= semaforos_i.msb(33);
		semaforos_o.lsb(33) <= sem_lsb_o_34;
		semaforos_o.msb(33) <= sem_msb_o_34;
		sem_lsb_i_35 <= semaforos_i.lsb(34);
		sem_msb_i_35 <= semaforos_i.msb(34);
		semaforos_o.lsb(34) <= sem_lsb_o_35;
		semaforos_o.msb(34) <= sem_msb_o_35;
		sem_lsb_i_36 <= semaforos_i.lsb(35);
		sem_msb_i_36 <= semaforos_i.msb(35);
		semaforos_o.lsb(35) <= sem_lsb_o_36;
		semaforos_o.msb(35) <= sem_msb_o_36;
end Behavioral;
