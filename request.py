class Contato(Recursion):
    def delete(self,id):
        conn = db.connect()
        conn.execute("delete from contatos where id=%d" %int(id))
        return {"status";"sucess"}

    def get(self,id):
        conn = db.connect()
        conn.execute("select * from contatos where id=%d" %int(id))
        result = [dict(zip(tuple(query.keys()),i))for i in query.cursor]
        return jsonify(result)

    def get(self,nome):
        conn = db.connect()
        conn.execute("select * from contatos where nome=%s" %str(nome))
        result = [dict(zip(tuple(query.keys()),i))for i in query.cursor]
        return jsonify(result)