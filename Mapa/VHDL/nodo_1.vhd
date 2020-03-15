-- nodo_1.vhdl : Achivo VHDL generado automaticamente
library IEEE;
use IEEE.std_logic_1164.all;
use IEEE.numeric_std.all;
--Declare the package
use work.my_package.all;
	entity nodo_1 is
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
			Estado_post :  out std_logic;
			Semaforo_propio_i_1 :  in sem_type;
			Semaforo_propio_o_1 :  out sem_type;
			Semaforo_cercano :  out sem_type;
			Semaforo_lejano :  out sem_type;
			Estado_o :  out std_logic
		);
	end entity nodo_1;
architecture Behavioral of nodo_1 is
begin
	process(Clock,Reset)
	begin
		if (Clock = '1' and Clock'Event) then
			if (Reset = '1') then
				Estado_o <= '0';
				Semaforo_propio_o_1.msb <= '0';
				Semaforo_propio_o_1.lsb <= '0';
			else
				Estado_o <= Estado_i;
				Semaforo_propio_o_1.msb <= Semaforo_propio_i_1.msb;
				Semaforo_propio_o_1.lsb <= Semaforo_propio_i_1.lsb;
			end if;
		end if;
	end process;
end Behavioral;