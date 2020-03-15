-- nodo_3.vhdl : Achivo VHDL generado automaticamente
library IEEE;
use IEEE.std_logic_1164.all;
use IEEE.numeric_std.all;
--Declare the package
use work.my_package.all;
	entity nodo_3 is
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
			Estado_ante :  out std_logic;
			Estado_post :  out std_logic;
			Semaforo_cercano :  out sem_type;
			Semaforo_lejano :  out sem_type;
			Estado_o :  out std_logic
		);
	end entity nodo_3;
architecture Behavioral of nodo_3 is
begin
	process(Clock,Reset)
	begin
		if (Clock = '1' and Clock'Event) then
			if (Reset = '1') then
				Estado_o <= '0';
			else
				Estado_o <= Estado_i;
			end if;
		end if;
	end process;
end Behavioral;