-- nodo_5.vhdl : Achivo VHDL generado automaticamente
library IEEE;
use IEEE.std_logic_1164.all;
use IEEE.numeric_std.all;
--Declare the package
use work.my_package.all;
	entity nodo_5 is
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
			Estado_o :  out std_logic
		);
	end entity nodo_5;
architecture Behavioral of nodo_5 is
begin
	process(Clock,Reset)
	begin
		if (Clock = '1' and Clock'Event) then
			if (Reset = '1') then
				Semaforo_propio_o_1.msb <= '0';
				Semaforo_propio_o_1.lsb <= '0';
			else
				Estado_o <= Estado_i;
				if ( Estado_i = '0' ) then
					Semaforo_propio_o_1.msb <= '0';
					Semaforo_propio_o_1.lsb <= '0';
				else
					Semaforo_propio_o_1.msb <= '1';
					Semaforo_propio_o_1.lsb <= '0';
				end if;
			end if;
		end if;
	end process;
end Behavioral;