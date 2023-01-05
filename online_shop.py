
new= ['t-shirt','pants','glass']
done = []
class Shop:
    

    def __init__(self,new,done):
        self.new = new
        self.done = done
    def in_process(self,new,done):
        while self.new:
            currently=new.pop()
            print(f'{currently} is packing, change category to done')
            done.append(currently)

    def ready(self,done):
        for ready in done:
            print(f'{ready} done, packed, ready to send :)')


client1 = Shop(new,done)
client1.in_process(new,done)
client1.ready(done)
