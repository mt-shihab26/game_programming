#pragma once

class VertexBuffer {
  private:
    unsigned int m_renderer_id;

  public:
    VertexBuffer(const void *data, unsigned int size);
    ~VertexBuffer();

    void bind() const;
    void unbind() const;

    inline unsigned int get_renderer_id() const { return m_renderer_id; }
};
