-- nodo_5.vhdl : Achivo VHDL generado automaticamente
library IEEE;
use IEEE.std_logic_1164.all;
use IEEE.numeric_std.all;
--Declare the package
use work.my_package.all;
	entity nodo_5 is
		generic(
			N : natural := 32;
			N_SEM : natural := 10;
			N_MDC : natural := 2;
			N_CVS : natural := 10
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
			Semaforo_cercano_3_i :  in sem_type;
			Semaforo_cercano_8_i :  in sem_type;
			Semaforo_cercano_7_i :  in sem_type;
			Estado_lejano_3_i :  in std_logic;
			Estado_lejano_8_i :  in std_logic;
			Estado_lejano_7_i :  in std_logic;
			Estado_o :  out std_logic
		);
	end entity nodo_5;
architecture Behavioral of nodo_5 is
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
					if (Cambio_i = '0') then --Normal
						if Estado_ante = '0' then
							--estado = ROJO
							Semaforo_propio_o_1.msb <= '0'; --ROJO
							Semaforo_propio_o_1.lsb <= '0'; --ROJO
						else
							--Si OTRO = OCUPADO
							if (Estado_lejano_3_i = '0') then
								--estado = AMARILLO
								Semaforo_propio_o_1.msb <= '1'; --AMARILLO
								Semaforo_propio_o_1.lsb <= '0'; --AMARILLO
							else
								--estado = VERDE
								Semaforo_propio_o_1.msb <= '1'; --VERDE
								Semaforo_propio_o_1.lsb <= '1'; --VERDE
							end if;
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
	Semaforo_2 : process(Clock,Reset)
	begin
		if (Clock = '1' and Clock'Event) then
			if (Reset = '1') then
				Semaforo_propio_o_2.msb <= '0';
				Semaforo_propio_o_2.lsb <= '0';
			else
				if ( Estado_i = '0' ) then
					--estado = ROJO
					Semaforo_propio_o_2.msb <= '0'; --ROJO
					Semaforo_propio_o_2.lsb <= '0'; --ROJO
				else
					if (Cambio_i = '0') then --Normal
						if Estado_post = '0' then
							--estado = ROJO
							Semaforo_propio_o_2.msb <= '0'; --ROJO
							Semaforo_propio_o_2.lsb <= '0'; --ROJO
						else
							--Si OTRO = OCUPADO
							if (Estado_lejano_8_i = '0') then
								--estado = AMARILLO
								Semaforo_propio_o_2.msb <= '1'; --AMARILLO
								Semaforo_propio_o_2.lsb <= '0'; --AMARILLO
							else
								--estado = VERDE
								Semaforo_propio_o_2.msb <= '1'; --VERDE
								Semaforo_propio_o_2.lsb <= '1'; --VERDE
							end if;
						end if;
					else
						--estado = ROJO
						Semaforo_propio_o_2.msb <= '0'; --ROJO
						Semaforo_propio_o_2.lsb <= '0'; --ROJO
					end if;
				end if;
			end if;
		end if;
	end process;
	Semaforo_3 : process(Clock,Reset)
	begin
		if (Clock = '1' and Clock'Event) then
			if (Reset = '1') then
				Semaforo_propio_o_3.msb <= '0';
				Semaforo_propio_o_3.lsb <= '0';
			else
				if ( Estado_i = '0' ) then
					--estado = ROJO
					Semaforo_propio_o_3.msb <= '0'; --ROJO
					Semaforo_propio_o_3.lsb <= '0'; --ROJO
				else
					if (Cambio_i = '0') then --Normal
						if Estado_ante = '0' then
							--estado = AMARILLO
							Semaforo_propio_o_3.msb <= '1'; --AMARILLO
							Semaforo_propio_o_3.lsb <= '0'; --AMARILLO
						else
							--Si Color = AMARILLO
							if (Semaforo_cercano_7_i.msb = '1' and  Semaforo_cercano_7_i.lsb = '0') then
								--estado = VERDE
								Semaforo_propio_o_3.msb <= '1'; --VERDE
								Semaforo_propio_o_3.lsb <= '1'; --VERDE
							else
								--estado = VERDE
								Semaforo_propio_o_3.msb <= '1'; --VERDE
								Semaforo_propio_o_3.lsb <= '1'; --VERDE
							end if;
						end if;
					else
						--estado = ROJO
						Semaforo_propio_o_3.msb <= '0'; --ROJO
						Semaforo_propio_o_3.lsb <= '0'; --ROJO
					end if;
				end if;
			end if;
		end if;
	end process;
end Behavioral;