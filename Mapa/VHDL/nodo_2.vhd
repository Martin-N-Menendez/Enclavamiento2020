-- nodo_2.vhdl : Achivo VHDL generado automaticamente
library IEEE;
use IEEE.std_logic_1164.all;
use IEEE.numeric_std.all;
--Declare the package
use work.my_package.all;
	entity nodo_2 is
		generic(
			N : natural := 21;
			N_SEM : natural := 7;
			N_MDC : natural := 1;
			N_CVS : natural := 6
		);
		port(
			Clock :  in std_logic;
			Reset :  in std_logic;
			Cambio_i :  in std_logic;
			Estado_i :  in std_logic;
			Estado_ante :  in std_logic;
			Estado_post :  in std_logic;
			Semaforo_propio_i_1 :  in sem_type;
			Semaforo_propio_o_1 :  out sem_type;
			Semaforo_propio_i_2 :  in sem_type;
			Semaforo_propio_o_2 :  out sem_type;
			Semaforo_propio_i_3 :  in sem_type;
			Semaforo_propio_o_3 :  out sem_type;
			Semaforo_cercano_1_i :  in sem_type;
			Semaforo_cercano_5_i :  in sem_type;
			Semaforo_cercano_6_i :  in sem_type;
			Estado_o :  out std_logic
		);
	end entity nodo_2;
architecture Behavioral of nodo_2 is
begin
	process(Clock,Reset)
	begin
		if (Clock = '1' and Clock'Event) then
			if (Reset = '1') then
				Semaforo_propio_o_1.msb <= '0';
				Semaforo_propio_o_1.lsb <= '0';
				Semaforo_propio_o_2.msb <= '0';
				Semaforo_propio_o_2.lsb <= '0';
				Semaforo_propio_o_3.msb <= '0';
				Semaforo_propio_o_3.lsb <= '0';
			else
				Estado_o <= Estado_i;
				if ( Estado_i = '0' ) then
					Semaforo_propio_o_1.msb <= '0';
					Semaforo_propio_o_1.lsb <= '0';
					Semaforo_propio_o_2.msb <= '0';
					Semaforo_propio_o_2.lsb <= '0';
					Semaforo_propio_o_3.msb <= '0';
					Semaforo_propio_o_3.lsb <= '0';
				else
					Semaforo_propio_o_1.msb <= '1';
					Semaforo_propio_o_1.lsb <= '0';
					Semaforo_propio_o_2.msb <= '1';
					Semaforo_propio_o_2.lsb <= '0';
					Semaforo_propio_o_3.msb <= '1';
					Semaforo_propio_o_3.lsb <= '0';
				 --2 con 1
				 --2 en ['T', 'N', 'R', 'R']
				 --2 con 5
				 --2 en ['T', 'N', 'R', 'R']
				 --2 con 6
				 --2 en ['T', 'N', 'R', 'R']
				end if;
			end if;
		end if;
	end process;
end Behavioral;