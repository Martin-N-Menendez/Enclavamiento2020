-- nodo_19.vhdl : Achivo VHDL generado automaticamente
library IEEE;
use IEEE.std_logic_1164.all;
use IEEE.numeric_std.all;
--Declare the package
use work.my_package.all;
	entity nodo_19 is
		generic(
			N : natural := 90;
			N_SEM : natural := 27;
			N_MDC : natural := 12;
			N_CVS : natural := 24
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
			Semaforo_cercano_1_i :  in sem_type;
			Semaforo_cercano_10_i :  in sem_type;
			Semaforo_cercano_1_i :  in sem_type;
			Estado_lejano_1_i :  in std_logic;
			Estado_lejano_10_i :  in std_logic;
			Estado_lejano_1_i :  in std_logic;
			Estado_o :  out std_logic
		);
	end entity nodo_19;
architecture Behavioral of nodo_19 is
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
					if (Cambio_i = '1') then --Reverso
						if Estado_ante = '0' then
							--estado = ROJO
							Semaforo_propio_o_1.msb <= '0'; --ROJO
							Semaforo_propio_o_1.lsb <= '0'; --ROJO
						else
							--estado = AMARILLO
							Semaforo_propio_o_1.msb <= '1'; --AMARILLO
							Semaforo_propio_o_1.lsb <= '0'; --AMARILLO
						end if;
					else
						--estado = ROJO
						Semaforo_propio_o_1.msb <= '0'; --ROJO
						Semaforo_propio_o_1.lsb <= '0'; --ROJO
					end if;
				end if;
			end if;
		end if;
	end process;
end Behavioral;