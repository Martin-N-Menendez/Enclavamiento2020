library IEEE;
use IEEE.std_logic_1164.all;
use IEEE.numeric_std.all;

entity detector is
	port(
		clk_i: in std_logic;
        rst_i: in std_logic;
		r_data: in std_logic_vector(8-1 downto 0);
		led_rgb_1  : out std_logic_vector(3-1 downto 0);
		led_rgb_2  : out std_logic_vector(3-1 downto 0);
		paquete: out std_logic_vector(23-1 downto 0);
		w_data: out std_logic_vector(8-1 downto 0)
	);
end detector;

architecture Behavioral of detector is
    
    type estados_t is (inicio,lectura,final,error);
    signal estado, estado_siguiente : estados_t; 
  
    signal char_data : std_logic_vector(8-1 downto 0);
    
    signal contador: std_logic_vector(3 downto 0);
    
begin
    
    process(clk_i)
    begin
        if (clk_i = '1' and clk_i'event) then
            if rst_i = '1' then          
                estado <= inicio;
            else
                estado <= estado_siguiente;       
            end if;
        end if;
    end process;
   
   process(clk_i,r_data) 
   begin 
        if (clk_i = '1' and clk_i'event) then
            if rst_i = '1' then          
                contador <= (others => '0'); 
            else
                if r_data = "00111100" then 
                    contador <= (others => '0');
                else
                    if r_data /= "00111100"then
                        char_data <= r_data;
                        if char_data /= r_data then
                            contador <= std_logic_vector(unsigned(contador) + 1); 
                        end if;  
                    end if; 
                end if;
            end if;
        end if;             
    end process;
   
     process(estado,r_data,contador)      
     begin
 
        estado_siguiente <= estado;   
        -- LED4 = RGB2 | LED5 => RGB1
        -- BGR -> 001 = R | 010 = G | 100 = B
        case(estado) is                  
                    
          when inicio =>        
            led_rgb_1 <= "100";   -- azul LD5
            --led_rgb_2 <= "100"; -- azul LD4
            if r_data = "00111100" then -- r_data = '<'
                estado_siguiente <= lectura;                    
            end if;               
          when lectura =>  
            if contador = "1000" then
                if r_data = "00111110" then --  r_data = '>'                  
                  estado_siguiente <= final;
                else
                  estado_siguiente <= error;                
               end if;                      
            else
                led_rgb_1 <= "101"; -- azul
                led_rgb_2 <= "100"; -- azul
            end if;         
          when final =>  
            --led_rgb_1 <= "111"; -- blanco   
            led_rgb_2 <= "010"; -- verde
            if r_data = "00111100" then -- r_data = '<'
                estado_siguiente <= lectura;                    
            end if;           
          when error => 
            --led_rgb_1 <= "111"; -- blanco        
            led_rgb_2 <= "001"; -- rojo
            if r_data = "00111100" then -- r_data = '<'
                estado_siguiente <= lectura;                    
            end if;                
          when others => null;
        end case;
      end process;
    
--    process(clk_i)
--    begin
--        if rising_edge(clk_i) then
--            if rst_i = '1' then
--                char_data <= "00000000";
--            else                 
--                char_data <= r_data;
--            end if;
--        end if;
--    end process;
    
    --char_data <= r_data;
    w_data <= r_data;      
        
end Behavioral;
