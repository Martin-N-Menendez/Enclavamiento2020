-- nodo_14.vhdl : Achivo VHDL generado automaticamente
library IEEE;
use IEEE.std_logic_1164.all;
use IEEE.numeric_std.all;
--Declare the package
use work.my_package.all;
	entity nodo_14 is
		generic(
			N : natural := 50;
			N_SEM : natural := 16;
			N_MDC : natural := 4;
			N_CVS : natural := 14
		);
		port(
			Clock :  in std_logic;
			Reset :  in std_logic;
			Estado_i :  in std_logic;
			Estado_post :  in std_logic;
			Semaforo_propio_i_1 :  in sem_type;
			Semaforo_propio_o_1 :  out sem_type;
			Estado_o :  out std_logic
		);
	end entity nodo_14;
architecture Behavioral of nodo_14 is
begin
	Estado_o <= Estado_i;
	Semaforo_1 : process(Clock,Reset)
	begin
		if (Clock = '1' and Clock'Event) then
			if (Reset = '1') then
				Semaforo_propio_o_1.msb <= '0';
				Semaforo_propio_o_1.lsb <= '0';
			else
				if ( Estado_i = '0' ) then
					--estado = ROJO
					Semaforo_propio_o_1.msb <= '0'; --ROJO
					Semaforo_propio_o_1.lsb <= '0'; --ROJO
				else
					--estado = VERDE
					Semaforo_propio_o_1.msb <= '1'; --VERDE
					Semaforo_propio_o_1.lsb <= '1'; --VERDE
				end if;
			end if;
		end if;
	end process;
end Behavioral;