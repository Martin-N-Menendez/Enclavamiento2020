library IEEE;
use IEEE.std_logic_1164.all;
use IEEE.numeric_std.all;

entity fifo_enclavamiento is
	port(
		clk_i: in std_logic;
        rst_i: in std_logic;
        paquete_i: in std_logic_vector(17-1 downto 0);
        w_data: out std_logic_vector(8-1 downto 0)
	);
    end entity;

architecture Behavioral of fifo_enclavamiento is
    
    --type estados_t is (permitido,prohibido);
    --signal estado, estado_siguiente : estados_t;
  
    signal char_data : std_logic_vector(8-1 downto 0);
    signal paquete_aux: std_logic_vector(17-1 downto 0);
    signal contador: std_logic_vector(8-1 downto 0);
    signal estado : std_logic;
begin    
        
    process(clk_i)
    begin
        if (clk_i = '1' and clk_i'event) then
            if rst_i = '1' then
                char_data <= "00000000";
            else          
                if estado = '1' then     
                    if paquete_i(16-to_integer(unsigned(contador))) = '0' then                 
                        w_data <= "00110000";
                    end if;
                    if paquete_i(16-to_integer(unsigned(contador))) = '1' then                 
                        w_data <= "00110001";
                    end if; 
                                                       
                        --w_data <= char_data;
                 end if;
            end if;
        end if;
    end process;
    
   process(clk_i) 
   begin 
        if (clk_i = '1' and clk_i'event) then
            if rst_i = '1' then          
                contador <= (others => '0');
                estado <= '1'; 
            else
            
                if estado = '1' then
                    contador <= std_logic_vector(unsigned(contador) + 1);
                    if contador = "00010000" then
                        estado <= '0';  
                    end if;
                else 
                    contador <= std_logic_vector(unsigned(contador) + 0);
                end if;
                
                paquete_aux <= paquete_i;
                if paquete_aux /= paquete_i then
                    contador <= (others => '0'); 
                    estado <= '1';
                end if;
                       
            end if;
        end if;             
    end process;
    

    --w_data <= "01100001";
    --  w_data <= char_data;
        
end Behavioral;
